from pydantic import BaseModel


class JobImport(BaseModel):
    provider: str
    provider_job_id: str

    title: str

    company_name: str

    company_website: str | None = None

    location: str | None = None

    description: str | None = None

    employment_type: str | None = None

    job_url: str

    posted_at: str | None = None