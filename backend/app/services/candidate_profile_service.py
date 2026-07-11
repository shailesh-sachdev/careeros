from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.candidate_profile import CandidateProfile


class CandidateProfileService:

    def get(self, db: Session) -> CandidateProfile | None:
        return db.scalar(select(CandidateProfile))

    def create(
        self,
        db: Session,
        profile_data: dict,
    ) -> CandidateProfile:

        profile = CandidateProfile(**profile_data)
        db.add(profile)
        db.commit()
        db.refresh(profile)

        return profile

    def update(
        self,
        db: Session,
        existing: CandidateProfile,
        data: dict,
    ) -> CandidateProfile:

        for key, value in data.items():
            setattr(existing, key, value)

        db.commit()
        db.refresh(existing)

        return existing