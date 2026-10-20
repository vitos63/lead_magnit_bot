from sqlalchemy.ext.asyncio import AsyncSession

from bot import bot
from bot.texts.admin import format_diagnostics, format_review_request
from bot.texts.answers import format_questionnaire
from bot.texts.result import format_result
from core.settings import settings
from models.enums import Stage
from repo.pre_questionnaire import PreQuestionnaireRepository
from repo.user import UserRepository
from schemas.pre_questionnaire import PRE_QUESTION_TEXTS, PreQuestion, PreQuestionAnswer
from services.first_questions import FirstQuestionsService
from utils.answers import collect_answers


class PreQuestionnaireService:
    def __init__(self, session: AsyncSession):
        self.repository = PreQuestionnaireRepository(session)
        self.user_repository = UserRepository(session)
        self.first_questions = FirstQuestionsService(session)

    async def open(self, tg_id: int) -> None:
        await self.user_repository.advance_stage(tg_id, Stage.OPEN_PRE_QUESTIONNAIRE)

    async def save_answer(self, item: PreQuestionAnswer) -> None:
        if item.question == PreQuestion.CONTACT:
            await self.user_repository.set_contact(item.tg_id, item.answer)
        else:
            await self.repository.set_answer(item.tg_id, item.question, item.answer)

    async def get_answers(self, tg_id: int) -> dict[str, bool | str]:
        user = await self.user_repository.get(tg_id)
        return collect_answers(await self.repository.get(tg_id), user.contact)

    async def send(self, tg_id: int) -> None:
        user = await self.user_repository.get(tg_id)
        result = format_result(await self.first_questions.repository.get_scores(tg_id))
        answers = format_questionnaire(PRE_QUESTION_TEXTS, await self.get_answers(tg_id))
        diagnostics = await self.first_questions.format_answers(tg_id)
        await bot.send_message(settings.ADMIN_TG_ID, format_review_request(user, result, answers))
        await bot.send_message(settings.ADMIN_TG_ID, format_diagnostics(user, diagnostics))
        await self.user_repository.give_consent(tg_id)
        await self.user_repository.advance_stage(tg_id, Stage.SEND_PRE_QUESTIONNAIRE)
