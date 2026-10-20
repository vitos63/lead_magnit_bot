from models import FirstQuestions
from repo.answers import AnswersRepository
from schemas.first_questions import Scores


class FirstQuestionsRepository(AnswersRepository):
    model = FirstQuestions

    async def get_scores(self, tg_id: int) -> Scores | None:
        questions = await self.get(tg_id)
        return Scores.model_validate(questions.scores) if questions and questions.scores else None

    async def set_scores(self, tg_id: int, scores: dict) -> None:
        questions = await self.get(tg_id)
        questions.scores = scores
        await self.session.commit()
