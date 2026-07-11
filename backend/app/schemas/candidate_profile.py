from pydantic import BaseModel


class CandidateProfileBase(BaseModel):
    full_name: str
    headline: str | None = None
    summary: str | None = None
    preferred_location: str | None = None
    remote_only: bool = False
    years_experience: int | None = None


class CandidateProfileCreate(CandidateProfileBase):
    pass


class CandidateProfileUpdate(BaseModel):
    full_name: str | None = None
    headline: str | None = None
    summary: str | None = None
    preferred_location: str | None = None
    remote_only: bool | None = None
    years_experience: int | None = None


class CandidateProfileResponse(CandidateProfileBase):
    id: int

    model_config = {
        "from_attributes": True
    }