from sqlalchemy.ext.asyncio import AsyncSession

from repo.first_questions import FirstQuestionsRepository
from schemas.first_questions import QuestionAnswer


class FirstQuestionsService:
    def __init__(self, session: AsyncSession):
        self.repository = FirstQuestionsRepository(session)

    async def save_answer(self, item: QuestionAnswer) -> None:
        await self.repository.set_answer(item.tg_id, item.question, item.answer)
