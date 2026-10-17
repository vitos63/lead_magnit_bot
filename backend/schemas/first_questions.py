from typing import Literal

from pydantic import BaseModel

Question = Literal[
    "has_product",
    "product_description",
    "ten_seconds",
    "has_offer",
    "offer_description",
    "channels",
    "main_channel",
    "tries",
    "thirty",
    "has_next_step",
    "pin_post",
    "client_must_to_do",
]


class QuestionAnswer(BaseModel):
    tg_id: int
    question: Question
    answer: bool | str
