from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.application import Application, ApplicationStatus


class ApplicationService:

    def create(
        self,
        db: Session,
        job_id: int,
    ) -> Application:

        existing = self.get_by_job(
            db=db,
            job_id=job_id,
        )

        if existing:
            return existing

        application = Application(
            job_id=job_id,
            status=ApplicationStatus.SAVED,
        )

        db.add(application)
        db.commit()
        db.refresh(application)

        return application

    def get(
        self,
        db: Session,
        application_id: int,
    ) -> Application | None:

        return db.scalar(
            select(Application).where(
                Application.id == application_id
            )
        )

    def update_status(
        self,
        db: Session,
        application: Application,
        status: ApplicationStatus,
    ) -> Application:

        application.status = status

        db.commit()
        db.refresh(application)

        return application
    
    def delete(
        self,
        db: Session,
        application: Application,
    ) -> None:

        db.delete(application)
        db.commit()

    def get_by_job(
        self,
        db: Session,
        job_id: int,
    ) -> Application | None:

        return db.scalar(
            select(Application).where(
                Application.job_id == job_id
            )
        )