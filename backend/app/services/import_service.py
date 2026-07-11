from app.providers.base import BaseProvider
from app.schemas.job_import import JobImport


class ImportService:
    async def import_jobs(
        self,
        provider: BaseProvider,
        **kwargs,
    ) -> list[JobImport]:
        jobs = await provider.fetch_jobs(**kwargs)
        return jobs