from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from repo.user import UserRepository


class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def get(self, tg_id: int) -> User | None:
        return await self.repository.get(tg_id)

    async def set_start_message_id(self, tg_id: int, message_id: int) -> None:
        await self.repository.set_start_message_id(tg_id, message_id)

    async def skip_review(self, tg_id: int) -> None:
        await self.repository.skip_review(tg_id)

    async def get_or_add(self, user: User) -> User:
        existing = await self.repository.get(user.tg_id)
        if existing:
            return existing
        await self.repository.add(user)
        return user
