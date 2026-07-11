from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload

from app.models.job import Job


class JobQueryService:

    def list_jobs(
        self,
        db: Session,
        page: int,
        page_size: int,
    ):

        total = db.scalar(
            select(func.count()).select_from(Job)
        )

        statement = (
            select(Job)
            .options(joinedload(Job.company))
            .order_by(Job.created_at.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
        )

        jobs = list(
            db.scalars(statement).unique().all()
        )

        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "items": jobs,
        }