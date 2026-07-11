from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.company import Company


class CompanyService:

    def get_or_create(
        self,
        db: Session,
        name: str,
        website: str | None = None,
    ) -> Company:

        company = db.scalar(
            select(Company).where(
                Company.name == name
            )
        )

        if company:
            return company

        company = Company(
            name=name,
            website=website,
        )

        db.add(company)

        db.flush()

        return company