from abc import ABC, abstractmethod

from app.schemas.job_import import JobImport


class BaseProvider(ABC):

    @abstractmethod
    async def fetch_jobs(self) -> list[JobImport]:
        pass