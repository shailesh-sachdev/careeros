from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload

from app.models.job import Job
from app.models.company import Company
from sqlalchemy import func, or_, select


class JobQueryService:


    def list_jobs(
        self,
        db: Session,
        page: int,
        page_size: int,
        search: str | None = None,
    ):

        statement = (
            select(Job)
            .join(Job.company)
            .options(joinedload(Job.company))
        )

        if search:

            search_term = f"%{search}%"

            statement = statement.where(
                or_(
                    Job.title.ilike(search_term),
                    Job.location.ilike(search_term),
                    Company.name.ilike(search_term),
                )
            )

        total = db.scalar(
            select(func.count()).select_from(statement.subquery())
        )

        jobs = list(
            db.scalars(
                statement.order_by(Job.created_at.desc())
                .offset((page - 1) * page_size)
                .limit(page_size)
            )
            .unique()
            .all()
        )

        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "items": jobs,
        }