from models import FirstQuestions
from repo.answers import AnswersRepository


class FirstQuestionsRepository(AnswersRepository):
    model = FirstQuestions
