from sqlalchemy.ext.asyncio import AsyncSession

from bot.texts.result import format_scores
from models import User
from repo.user import UserRepository
from schemas.admin import AdminUser, AdminUserCard
from schemas.first_questions import Question, Scores
from utils import collect_answers, extract_answers


class AdminService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def get_users(self) -> list[AdminUser]:
        return [self.build(AdminUser, user) for user in await self.repository.get_all_with_answers()]

    async def get_user(self, tg_id: int) -> AdminUserCard | None:
        user = await self.repository.get_with_answers(tg_id)
        return self.build(AdminUserCard, user) if user else None

    @staticmethod
    def build[T: AdminUser](schema: type[T], user: User) -> T:
        first_answers = extract_answers(user.first_questions, Question)
        pre_answers = collect_answers(user.pre_questionnaire, user.contact)
        scores = user.first_questions and user.first_questions.scores
        return schema(
            tg_id=user.tg_id,
            username=user.username,
            start_date=user.start_date,
            stage=user.stage,
            skipped_review=user.skipped_review,
            first_answers_count=len(first_answers),
            pre_answers_count=len(pre_answers),
            payments=user.payments,
            contact=user.contact,
            scores=scores and format_scores(Scores.model_validate(scores)),
            first_answers=first_answers,
            pre_answers=pre_answers,
        )
