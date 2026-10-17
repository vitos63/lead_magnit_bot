from sqlalchemy.ext.asyncio import AsyncSession

from bot import bot
from bot.keyboards.review import REVIEW_KEYBOARD
from bot.texts.result import format_result
from clients.ai.openrouter import openrouter
from clients.ai.prompts import RESULT_PROMPT
from database import SessionLocal
from models.enums import Stage
from repo.first_questions import FirstQuestionsRepository
from repo.user import UserRepository
from schemas.first_questions import QUESTION_TEXTS, QuestionAnswer, Scores


class FirstQuestionsService:
    def __init__(self, session: AsyncSession):
        self.repository = FirstQuestionsRepository(session)

    async def save_answer(self, item: QuestionAnswer) -> None:
        await self.repository.set_answer(item.tg_id, item.question, item.answer)

    async def get_answers(self, tg_id: int) -> str:
        questions = await self.repository.get(tg_id)
        return "\n\n".join(
            f"{number}. {text}\nОтвет: {self.format_answer(getattr(questions, question.value))}"
            for number, (question, text) in enumerate(QUESTION_TEXTS.items(), 1)
        )

    @staticmethod
    async def send_result(tg_id: int, answers: str) -> None:
        scores = Scores.model_validate_json(await openrouter.ask_json(RESULT_PROMPT, answers))
        await bot.send_message(tg_id, format_result(scores), reply_markup=REVIEW_KEYBOARD)
        async with SessionLocal() as session:
            await UserRepository(session).advance_stage(tg_id, Stage.GET_RESULT)

    @staticmethod
    def format_answer(answer: bool | str) -> str:
        if isinstance(answer, bool):
            return "Да" if answer else "Нет"
        return answer
