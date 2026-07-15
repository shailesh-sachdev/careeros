from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.ai.resume_parser import ResumeParser
from app.ai.resume_tailor import ResumeTailor
from app.db.dependencies import get_db
from app.models.job import Job
from app.models.resume import Resume


router = APIRouter(
    prefix="/resume-tailor",
    tags=["Resume Tailor"],
)


@router.post("/{resume_id}/{job_id}")
async def tailor_resume(
    resume_id: int,
    job_id: int,
    db: Session = Depends(get_db),
):

    resume = db.get(
        Resume,
        resume_id,
    )

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    job = db.get(
        Job,
        job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    parser = ResumeParser()

    resume_json = await parser.parse(
        resume.raw_text,
    )

    tailor = ResumeTailor()

    result = await tailor.tailor(
        resume_json=resume.parsed_data,
        job_title=job.title,
        department=job.department,
        job_description=job.description or "",
    )

    return {
        "tailored_resume": result,
    }