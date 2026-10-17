from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import FirstQuestions


class FirstQuestionsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, tg_id: int) -> FirstQuestions | None:
        return await self.session.scalar(select(FirstQuestions).where(FirstQuestions.tg_id == tg_id))

    async def get_answer(self, tg_id: int, question: str) -> bool | str | None:
        questions = await self.get(tg_id)
        return getattr(questions, question) if questions else None

    async def set_answer(self, tg_id: int, question: str, answer: bool | str) -> None:
        questions = await self.get(tg_id) or FirstQuestions(tg_id=tg_id)
        setattr(questions, question, answer)
        self.session.add(questions)
        await self.session.commit()
