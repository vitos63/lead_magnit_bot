from sqlalchemy.ext.asyncio import AsyncSession

from models.enums import Stage
from repo.pre_questionnaire import PreQuestionnaireRepository
from repo.user import UserRepository
from schemas.pre_questionnaire import PreQuestion, PreQuestionAnswer


class PreQuestionnaireService:
    def __init__(self, session: AsyncSession):
        self.repository = PreQuestionnaireRepository(session)
        self.user_repository = UserRepository(session)

    async def open(self, tg_id: int) -> None:
        await self.user_repository.advance_stage(tg_id, Stage.OPEN_PRE_QUESTIONNAIRE)

    async def save_answer(self, item: PreQuestionAnswer) -> None:
        if item.question == PreQuestion.CONTACT:
            await self.user_repository.set_contact(item.tg_id, item.answer)
        else:
            await self.repository.set_answer(item.tg_id, item.question, item.answer)

    async def get_answers(self, tg_id: int) -> dict[str, bool | str]:
        answers = await self.repository.get_answers(tg_id, PreQuestion)
        user = await self.user_repository.get(tg_id)
        if user.contact:
            answers[PreQuestion.CONTACT] = user.contact
        return answers

    async def send(self, tg_id: int) -> None:
        await self.user_repository.give_consent(tg_id)
        await self.user_repository.advance_stage(tg_id, Stage.SEND_PRE_QUESTIONNAIRE)
