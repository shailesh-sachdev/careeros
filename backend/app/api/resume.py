from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.candidate_profile import CandidateProfile
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


@router.post("/upload")
async def upload_resume(
    candidate_profile_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    profile = db.get(
        CandidateProfile,
        candidate_profile_id,
    )

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate profile not found",
        )

    service = ResumeService()

    return service.upload(
        db=db,
        candidate_profile_id=candidate_profile_id,
        file=file,
    )