from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.job import Job
from app.schemas.job_import import JobImport


class JobService:

    def get_by_provider_identity(
        self,
        db: Session,
        provider: str,
        provider_job_id: str,
    ) -> Job | None:

        return db.scalar(
            select(Job).where(
                Job.provider == provider,
                Job.provider_job_id == provider_job_id,
            )
        )

    def create(
        self,
        db: Session,
        company: Company,
        job: JobImport,
    ) -> Job:

        db_job = Job(
            company_id=company.id,
            provider=job.provider,
            provider_job_id=job.provider_job_id,
            title=job.title,
            location=job.location,
            employment_type=job.employment_type,
            job_url=job.job_url,
            description=job.description,
            department=job.department,
            team=job.team,
            requirements=job.requirements,
            responsibilities=job.responsibilities,
            benefits=job.benefits,
            posted_at=job.posted_at,
        )

        db.add(db_job)

        db.flush()

        return db_job

    def update(
        self,
        db: Session,
        db_job: Job,
        company: Company,
        job: JobImport,
    ) -> Job:

        db_job.company_id = company.id
        db_job.title = job.title
        db_job.location = job.location
        db_job.employment_type = job.employment_type
        db_job.job_url = job.job_url
        db_job.description = job.description
        db_job.department = job.department
        db_job.team = job.team
        db_job.requirements = job.requirements
        db_job.responsibilities = job.responsibilities
        db_job.benefits = job.benefits
        db_job.posted_at = job.posted_at

        db.flush()

        return db_job