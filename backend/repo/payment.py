from collections.abc import Sequence

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models import Payment


class PaymentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, payment_id: str) -> Payment | None:
        return await self.session.get(Payment, payment_id)

    async def get_paid_products(self, tg_id: int) -> Sequence[str]:
        query = (
            select(Payment.product)
            .where(Payment.tg_id == tg_id, Payment.status == "succeeded")
            .order_by(Payment.created_at)
        )
        return (await self.session.scalars(query)).all()

    async def add(self, payment: Payment) -> None:
        self.session.add(payment)
        await self.session.commit()

    async def set_status(self, payment_id: str, status: str) -> bool:
        result = await self.session.execute(
            update(Payment).where(Payment.id == payment_id, Payment.status != status).values(status=status)
        )
        await self.session.commit()
        return bool(result.rowcount)
