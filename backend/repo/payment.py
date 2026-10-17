from sqlalchemy.ext.asyncio import AsyncSession

from models import Payment


class PaymentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, payment_id: str) -> Payment | None:
        return await self.session.get(Payment, payment_id)

    async def add(self, payment: Payment) -> None:
        self.session.add(payment)
        await self.session.commit()

    async def set_status(self, payment_id: str, status: str) -> None:
        payment = await self.get(payment_id)
        payment.status = status
        await self.session.commit()
