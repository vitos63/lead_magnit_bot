from models import FirstQuestions
from repo.answers import AnswersRepository


class FirstQuestionsRepository(AnswersRepository):
    model = FirstQuestions

    async def set_scores(self, tg_id: int, scores: dict) -> None:
        questions = await self.get(tg_id)
        questions.scores = scores
        await self.session.commit()
