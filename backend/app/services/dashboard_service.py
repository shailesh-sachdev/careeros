from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.application import (
    Application,
    ApplicationStatus,
)
from app.models.job import Job


class DashboardService:

    def get_dashboard(
        self,
        db: Session,
    ) -> dict:

        total_applications = db.query(
            func.count(Application.id)
        ).scalar() or 0

        saved = db.query(
            func.count(Application.id)
        ).filter(
            Application.status == ApplicationStatus.SAVED
        ).scalar() or 0

        applied = db.query(
            func.count(Application.id)
        ).filter(
            Application.status == ApplicationStatus.APPLIED
        ).scalar() or 0

        interviews = db.query(
            func.count(Application.id)
        ).filter(
            Application.status == ApplicationStatus.INTERVIEW
        ).scalar() or 0

        offers = db.query(
            func.count(Application.id)
        ).filter(
            Application.status == ApplicationStatus.OFFER
        ).scalar() or 0

        accepted = db.query(
            func.count(Application.id)
        ).filter(
            Application.status == ApplicationStatus.ACCEPTED
        ).scalar() or 0

        rejected = db.query(
            func.count(Application.id)
        ).filter(
            Application.status == ApplicationStatus.REJECTED
        ).scalar() or 0

        recent_applications = (
            db.query(Application)
            .order_by(Application.created_at.desc())
            .limit(10)
            .all()
        )

        recent_jobs = (
            db.query(Job)
            .order_by(Job.created_at.desc())
            .limit(10)
            .all()
        )

        return {
            "applications": {
                "total": total_applications,
                "saved": saved,
                "applied": applied,
                "interview": interviews,
                "offer": offers,
                "accepted": accepted,
                "rejected": rejected,
            },
            "recent_jobs": [
                {
                    "id": job.id,
                    "title": job.title,
                    "company": job.company.name if job.company else None,
                    "location": job.location,
                    "created_at": job.created_at,
                }
                for job in recent_jobs
            ],
            "recent_applications": [
                {
                    "id": application.id,
                    "job_id": application.job_id,
                    "status": application.status.value,
                    "created_at": application.created_at,
                }
                for application in recent_applications
            ],
        }