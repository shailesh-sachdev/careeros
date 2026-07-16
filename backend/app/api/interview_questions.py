from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.ai.interview_questions import InterviewQuestionGenerator
from app.db.dependencies import get_db
from app.models.job import Job
from app.models.resume import Resume


router = APIRouter(
    prefix="/interview-questions",
    tags=["Interview Questions"],
)


@router.post("/{resume_id}/{job_id}")
async def generate_interview_questions(
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

    if resume.parsed_data is None:
        raise HTTPException(
            status_code=400,
            detail="Resume has not been parsed yet.",
        )

    generator = InterviewQuestionGenerator()

    questions = await generator.generate(
        resume_json=resume.parsed_data,
        job_title=job.title,
        department=job.department,
        job_description=job.description or "",
    )

    return questions