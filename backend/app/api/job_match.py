from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.ai.job_matcher import JobMatcher
from app.db.dependencies import get_db
from app.models.job import Job
from app.models.resume import Resume

router = APIRouter(
    prefix="/job-match",
    tags=["AI Job Match"],
)


@router.post("/{resume_id}/{job_id}")
async def match_job(
    resume_id: int,
    job_id: int,
    db: Session = Depends(get_db),
):

    resume = db.get(Resume, resume_id)

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    job = db.get(Job, job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    matcher = JobMatcher()

    return await matcher.match(
        resume_text=resume.raw_text,
        job_description=job.description or "",
    )