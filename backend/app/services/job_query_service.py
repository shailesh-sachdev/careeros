from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.job import Job


class JobQueryService:

    def list_jobs(
        self,
        db: Session,
    ) -> list[Job]:

        statement = (
            select(Job)
            .options(joinedload(Job.company))
            .order_by(Job.created_at.desc())
        )

        return list(db.scalars(statement).unique().all())