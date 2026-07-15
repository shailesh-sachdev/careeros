import httpx

from app.ai.base import BaseAIProvider
from app.core.config import settings


class OllamaProvider(BaseAIProvider):

    def __init__(self):
        self.base_url = settings.ollama_base_url
        self.model = settings.ollama_model

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        async with httpx.AsyncClient(timeout=40000) as client:

            response = await client.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": system_prompt,
                        },
                        {
                            "role": "user",
                            "content": user_prompt,
                        },
                    ],
                    "stream": False,
                },
            )

            response.raise_for_status()

            data = response.json()

            return data["message"]["content"]