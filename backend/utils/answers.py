from collections.abc import Iterable

from models import Base, PreQuestionnaire
from schemas.pre_questionnaire import PreQuestion


def extract_answers(answers: Base | None, questions: Iterable[str]) -> dict[str, bool | str]:
    return {question: answer for question in questions if (answer := getattr(answers, question, None)) is not None}


def collect_answers(pre_questionnaire: PreQuestionnaire | None, contact: str | None) -> dict[str, bool | str]:
    answers = extract_answers(pre_questionnaire, PreQuestion)
    if contact:
        answers[PreQuestion.CONTACT] = contact
    return answers
