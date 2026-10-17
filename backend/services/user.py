from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from repo.user import UserRepository


class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def add_if_not_exists(self, user: User) -> None:
        if not await self.repository.get(user.tg_id):
            await self.repository.add(user)
