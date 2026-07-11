from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.application import ApplicationStatus
from app.models.job import Job
from app.services.application_service import ApplicationService

router = APIRouter(
    prefix="/saved-jobs",
    tags=["Saved Jobs"],
)


@router.post("/{job_id}")
async def save_job(
    job_id: int,
    db: Session = Depends(get_db),
):
    job = db.get(Job, job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    service = ApplicationService()

    return service.create(
        db=db,
        job_id=job_id,
    )