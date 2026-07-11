from sqlalchemy.orm import Session

from app.providers.base import BaseProvider
from app.schemas.job_import import JobImport
from app.services.company_service import CompanyService
from app.services.job_service import JobService


class ImportService:

    async def import_jobs(
        self,
        db: Session,
        provider: BaseProvider,
        **kwargs,
    ) -> list[JobImport]:

        jobs = await provider.fetch_jobs(**kwargs)

        company_service = CompanyService()
        job_service = JobService()

        for job in jobs:

            company = company_service.get_or_create(
                db=db,
                name=job.company_name,
                website=job.company_website,
            )

            existing = job_service.get_by_provider_identity(
                db=db,
                provider=job.provider,
                provider_job_id=job.provider_job_id,
            )

            if existing:
                continue

            job_service.create(
                db=db,
                company=company,
                job=job,
            )

        db.commit()

        return jobs