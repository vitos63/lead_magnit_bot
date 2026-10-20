from datetime import datetime

from pydantic import BaseModel

from models.enums import Stage
from schemas.first_questions import Question
from schemas.pre_questionnaire import PreQuestion


class AdminUser(BaseModel):
    tg_id: int
    username: str | None
    start_date: datetime
    stage: Stage
    first_answers_count: int
    pre_answers_count: int


class AdminUserCard(AdminUser):
    contact: str | None
    scores: str | None
    first_answers: dict[Question, bool | str]
    pre_answers: dict[PreQuestion, bool | str]
