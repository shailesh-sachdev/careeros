from app.ai.providers.ollama import OllamaProvider
from app.core.config import settings


class AIManager:

    def __init__(self):

        if settings.ai_provider == "ollama":
            self.provider = OllamaProvider()
        else:
            raise ValueError(
                f"Unsupported AI provider: {settings.ai_provider}"
            )
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:

        return await self.provider.generate(
            system_prompt,
            user_prompt,
        )