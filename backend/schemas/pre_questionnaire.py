from enum import Enum

from pydantic import BaseModel


class PreQuestion(str, Enum):
    WHAT_RESULT_YOU_WANT_TO_GET = "what_result_you_want_to_get"
    WHAT_MOSTLY_HINDER = "what_mostly_hinder"
    ARE_YOU_READY = "are_you_ready"
    CONTACT = "contact"


PRE_QUESTION_TEXTS = {
    PreQuestion.WHAT_RESULT_YOU_WANT_TO_GET: "Какой результат вы хотите получить в ближайшие 2–3 месяца?",
    PreQuestion.WHAT_MOSTLY_HINDER: "Что сейчас больше всего мешает вам увеличить количество заявок?",
    PreQuestion.ARE_YOU_READY: "Готовы ли вы внедрять изменения в ближайший месяц?",
    PreQuestion.CONTACT: "Как с вами удобнее связаться?",
}


class PreQuestionAnswer(BaseModel):
    tg_id: int
    question: PreQuestion
    answer: bool | str
