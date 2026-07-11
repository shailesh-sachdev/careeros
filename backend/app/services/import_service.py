from sqlalchemy.orm import Session

from app.providers.base import BaseProvider
from app.schemas.job_import import JobImport
from app.services.company_service import CompanyService


class ImportService:

    async def import_jobs(
        self,
        db: Session,
        provider: BaseProvider,
        **kwargs,
    ) -> list[JobImport]:

        jobs = await provider.fetch_jobs(**kwargs)

        company_service = CompanyService()

        for job in jobs:

            company_service.get_or_create(
                db=db,
                name=job.company_name,
                website=job.company_website,
            )

        db.commit()

        return jobs