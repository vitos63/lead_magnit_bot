from uuid import uuid4

import httpx

from core.settings import settings
from schemas.payments import YooKassaPayment


class YooKassaClient:
    BASE_URL = "https://api.yookassa.ru/v3"
    VAT_CODE = 1

    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            auth=(settings.YOOKASSA_SHOP_ID, settings.YOOKASSA_SECRET_KEY),
            timeout=30,
        )

    async def create_payment(self, amount: int, description: str, return_url: str, metadata: dict) -> YooKassaPayment:
        value = {"value": f"{amount}.00", "currency": "RUB"}
        response = await self.client.post(
            "/payments",
            headers={"Idempotence-Key": str(uuid4())},
            json={
                "amount": value,
                "capture": True,
                "confirmation": {"type": "redirect", "return_url": return_url},
                "description": description,
                "metadata": metadata,
                "receipt": {
                    "customer": {"email": settings.RECEIPT_EMAIL},
                    "items": [
                        {
                            "description": description,
                            "quantity": 1,
                            "amount": value,
                            "vat_code": self.VAT_CODE,
                            "payment_subject": "service",
                            "payment_mode": "full_payment",
                        }
                    ],
                },
            },
        )
        response.raise_for_status()
        return YooKassaPayment.model_validate(response.json())

    async def get_payment(self, payment_id: str) -> YooKassaPayment:
        response = await self.client.get(f"/payments/{payment_id}")
        response.raise_for_status()
        return YooKassaPayment.model_validate(response.json())


yookassa = YooKassaClient()
