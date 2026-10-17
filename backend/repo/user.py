from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.enums import Stage


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, tg_id: int) -> User | None:
        return await self.session.get(User, tg_id)

    async def add(self, user: User) -> None:
        self.session.add(user)
        await self.session.commit()

    async def set_stage(self, tg_id: int, stage: Stage) -> None:
        user = await self.get(tg_id)
        user.stage = stage
        await self.session.commit()
