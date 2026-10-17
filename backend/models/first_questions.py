from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class FirstQuestions(Base):
    __tablename__ = "first_questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.tg_id"), unique=True)
    has_product: Mapped[bool | None]
    product_description: Mapped[str | None]
    ten_seconds: Mapped[bool | None]
    has_offer: Mapped[bool | None]
    offer_description: Mapped[str | None]
    channels: Mapped[str | None]
    main_channel: Mapped[bool | None]
    tries: Mapped[str | None]
    thirty: Mapped[bool | None]
    has_next_step: Mapped[bool | None]
    pin_post: Mapped[bool | None]
    client_must_to_do: Mapped[str | None]
