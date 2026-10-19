from contextlib import suppress

from aiogram.exceptions import TelegramBadRequest
from sqlalchemy.ext.asyncio import AsyncSession

from bot import bot
from bot.keyboards.review import REVIEW_KEYBOARD
from bot.texts.answers import format_questionnaire
from bot.texts.result import build_result, format_result
from clients.ai.openrouter import openrouter
from clients.ai.prompts import RESULT_PROMPT
from core.database import SessionLocal
from models.enums import Stage
from repo.first_questions import FirstQuestionsRepository
from repo.user import UserRepository
from schemas.first_questions import QUESTION_TEXTS, Question, QuestionAnswer, Result, Scores


class FirstQuestionsService:
    def __init__(self, session: AsyncSession):
        self.repository = FirstQuestionsRepository(session)

    async def save_answer(self, item: QuestionAnswer) -> None:
        await self.repository.set_answer(item.tg_id, item.question, item.answer)

    async def get_answers(self, tg_id: int) -> dict[str, bool | str]:
        return await self.repository.get_answers(tg_id, Question)

    async def format_answers(self, tg_id: int) -> str:
        return format_questionnaire(QUESTION_TEXTS, await self.get_answers(tg_id))

    async def get_result(self, tg_id: int) -> Result | None:
        questions = await self.repository.get(tg_id)
        if questions and questions.scores:
            return build_result(Scores.model_validate(questions.scores))
        return None

    @staticmethod
    async def send_result(tg_id: int, answers: str) -> None:
        scores = Scores.model_validate_json(await openrouter.ask_json(RESULT_PROMPT, answers))
        await bot.send_message(tg_id, format_result(scores), reply_markup=REVIEW_KEYBOARD)
        async with SessionLocal() as session:
            user_repository = UserRepository(session)
            await FirstQuestionsRepository(session).set_scores(tg_id, scores.model_dump())
            await user_repository.advance_stage(tg_id, Stage.GET_RESULT)
            user = await user_repository.get(tg_id)
        await FirstQuestionsService.remove_questions_button(tg_id, user.start_message_id)

    @staticmethod
    async def remove_questions_button(tg_id: int, message_id: int | None) -> None:
        if message_id:
            with suppress(TelegramBadRequest):
                await bot.edit_message_reply_markup(chat_id=tg_id, message_id=message_id)
