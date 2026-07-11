from sqlalchemy import asc, desc, func, or_, select
from sqlalchemy.orm import Session, joinedload

from app.models.company import Company
from app.models.job import Job


class JobQueryService:

    def list_jobs(
        self,
        db: Session,
        page: int,
        page_size: int,
        search: str | None = None,
        company: str | None = None,
        location: str | None = None,
        provider: str | None = None,
        sort: str = "newest",
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

        if company:
            statement = statement.where(
                Company.name.ilike(f"%{company}%")
            )

        if location:
            statement = statement.where(
                Job.location.ilike(f"%{location}%")
            )

        if provider:
            statement = statement.where(
                Job.provider == provider
            )

        total = db.scalar(
            select(func.count()).select_from(statement.subquery())
        )

        if sort == "oldest":
            statement = statement.order_by(
                asc(Job.created_at)
            )

        elif sort == "company":
            statement = statement.order_by(
                asc(Company.name)
            )

        elif sort == "title":
            statement = statement.order_by(
                asc(Job.title)
            )

        else:
            statement = statement.order_by(
                desc(Job.created_at)
            )

        jobs = list(
            db.scalars(
                statement
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