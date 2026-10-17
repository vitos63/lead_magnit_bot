from datetime import datetime

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.enums import Stage


class User(Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    username: Mapped[str | None]
    start_date: Mapped[datetime] = mapped_column(server_default=func.now())
    stage: Mapped[Stage] = mapped_column(default=Stage.START)
    consent: Mapped[bool] = mapped_column(default=False)
    contact: Mapped[str | None]
    subscription: Mapped[bool] = mapped_column(default=False)
    start_message_id: Mapped[int | None]
