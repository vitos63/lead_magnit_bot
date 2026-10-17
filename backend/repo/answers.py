from sqlalchemy.ext.asyncio import AsyncSession

from models import Base


class AnswersRepository:
    model: type[Base]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, tg_id: int):
        return await self.session.get(self.model, tg_id)

    async def set_answer(self, tg_id: int, question: str, answer: bool | str) -> None:
        answers = await self.get(tg_id) or self.model(tg_id=tg_id)
        setattr(answers, question, answer)
        self.session.add(answers)
        await self.session.commit()
