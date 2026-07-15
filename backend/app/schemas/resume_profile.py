from pydantic import BaseModel


class Experience(BaseModel):
    company: str
    role: str
    dates: str
    details: str


class Education(BaseModel):
    degree: str
    year: str | None = None


class Project(BaseModel):
    name: str
    details: str


class ResumeProfile(BaseModel):

    name: str

    email: str

    phone: str

    linkedin: str | None = None

    github: str | None = None

    summary: str

    skills: list[str]

    experience: list[Experience]

    education: list[Education]

    projects: list[Project]

    certifications: list[str] = []