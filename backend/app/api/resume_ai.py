from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.ai.resume_parser import ResumeParser
from app.db.dependencies import get_db
from app.models.resume import Resume

router = APIRouter(
    prefix="/resume-ai",
    tags=["Resume AI"],
)


@router.post("/parse/{resume_id}")
async def parse_resume(
    resume_id: int,
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

    parser = ResumeParser()

    result = await parser.parse(
        resume.raw_text,
    )

    return result