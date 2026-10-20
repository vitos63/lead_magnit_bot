from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.enums import Stage

if TYPE_CHECKING:
    from models import FirstQuestions, PreQuestionnaire


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

    first_questions: Mapped["FirstQuestions | None"] = relationship()
    pre_questionnaire: Mapped["PreQuestionnaire | None"] = relationship()
