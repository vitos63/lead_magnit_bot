from models import PreQuestionnaire
from repo.answers import AnswersRepository


class PreQuestionnaireRepository(AnswersRepository):
    model = PreQuestionnaire
