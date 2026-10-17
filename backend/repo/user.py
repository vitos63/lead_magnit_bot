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

    async def set_contact(self, tg_id: int, contact: str) -> None:
        user = await self.get(tg_id)
        user.contact = contact
        await self.session.commit()

    async def set_start_message_id(self, tg_id: int, message_id: int) -> None:
        user = await self.get(tg_id)
        user.start_message_id = message_id
        await self.session.commit()

    async def give_consent(self, tg_id: int) -> None:
        user = await self.get(tg_id)
        user.consent = True
        await self.session.commit()

    async def advance_stage(self, tg_id: int, stage: Stage) -> None:
        user = await self.get(tg_id)
        if list(Stage).index(stage) > list(Stage).index(user.stage):
            user.stage = stage
            await self.session.commit()
