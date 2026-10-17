from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from repo.user import UserRepository


class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def get(self, tg_id: int) -> User | None:
        return await self.repository.get(tg_id)

    async def get_or_add(self, user: User) -> User:
        existing = await self.repository.get(user.tg_id)
        if existing:
            return existing
        await self.repository.add(user)
        return user
