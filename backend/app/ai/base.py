from abc import ABC, abstractmethod


class BaseAIProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        pass