from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class PreQuestionnaire(Base):
    __tablename__ = "pre_questionnaire"

    tg_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.tg_id"), primary_key=True)
    what_result_you_want_to_get: Mapped[str | None]
    what_mostly_hinder: Mapped[str | None]
    are_you_ready: Mapped[bool | None]
