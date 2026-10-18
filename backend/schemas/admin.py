from datetime import datetime

from pydantic import BaseModel, ConfigDict

from models.enums import Stage
from schemas.first_questions import Question
from schemas.payments import Product
from schemas.pre_questionnaire import PreQuestion


class AdminPayment(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product: Product
    amount: int
    status: str
    created_at: datetime


class AdminUser(BaseModel):
    tg_id: int
    username: str | None
    start_date: datetime
    stage: Stage
    skipped_review: bool
    first_answers_count: int
    pre_answers_count: int
    payments: list[AdminPayment]


class AdminUserCard(AdminUser):
    contact: str | None
    scores: str | None
    first_answers: dict[Question, bool | str]
    pre_answers: dict[PreQuestion, bool | str]
