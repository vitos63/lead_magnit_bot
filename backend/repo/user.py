from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import User
from models.enums import Stage


class UserRepository:
    WITH_ANSWERS = (selectinload(User.first_questions), selectinload(User.pre_questionnaire))

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, tg_id: int) -> User | None:
        return await self.session.get(User, tg_id)

    async def get_with_answers(self, tg_id: int) -> User | None:
        return await self.session.get(User, tg_id, options=self.WITH_ANSWERS)

    async def get_all_with_answers(self) -> Sequence[User]:
        query = select(User).options(*self.WITH_ANSWERS).order_by(User.start_date.desc())
        return (await self.session.scalars(query)).all()

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
