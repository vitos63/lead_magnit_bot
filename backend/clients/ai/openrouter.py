import httpx

from settings import settings


class OpenRouterClient:
    MODELS = [
        "nvidia/nemotron-3-super-120b-a12b:free",
        "dots-studio/dots-3-note-preview:free",
        "google/gemma-4-31b-it:free",
    ]
    BASE_URL = "https://openrouter.ai/api/v1"

    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers={"Authorization": f"Bearer {settings.OPENROUTER_API_KEY}"},
            timeout=120,
        )

    async def ask_json(self, prompt: str, text: str) -> str:
        response = await self.client.post(
            "/chat/completions",
            json={
                "models": self.MODELS,
                "messages": [{"role": "system", "content": prompt}, {"role": "user", "content": text}],
                "response_format": {"type": "json_object"},
            },
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]


openrouter = OpenRouterClient()
