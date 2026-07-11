from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.candidate_profile import (
    CandidateProfileCreate,
    CandidateProfileResponse,
    CandidateProfileUpdate,
)
from app.services.candidate_profile_service import CandidateProfileService

router = APIRouter(
    prefix="/candidate-profile",
    tags=["Candidate Profile"],
)


@router.get("", response_model=CandidateProfileResponse)
async def get_profile(
    db: Session = Depends(get_db),
):
    service = CandidateProfileService()

    profile = service.get(db)

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate profile not found",
        )

    return profile


@router.post("", response_model=CandidateProfileResponse)
async def create_profile(
    profile: CandidateProfileCreate,
    db: Session = Depends(get_db),
):
    service = CandidateProfileService()

    return service.create(
        db=db,
        profile_data=profile.model_dump(),
    )


@router.put("", response_model=CandidateProfileResponse)
async def update_profile(
    data: CandidateProfileUpdate,
    db: Session = Depends(get_db),
):
    service = CandidateProfileService()

    profile = service.get(db)

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Candidate profile not found",
        )

    return service.update(
        db=db,
        existing=profile,
        data=data.model_dump(exclude_unset=True),
    )