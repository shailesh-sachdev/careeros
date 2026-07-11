from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.services.job_query_service import JobQueryService
from fastapi import HTTPException

from app.models.job import Job

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get("")
async def list_jobs(
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
    search: str | None = Query(None),
    company: str | None = Query(None),
    location: str | None = Query(None),
    provider: str | None = Query(None),
    sort: str = Query("newest"),
    db: Session = Depends(get_db),
):

    service = JobQueryService()

    return service.list_jobs(
        db=db,
        page=page,
        page_size=page_size,
        search=search,
        company=company,
        location=location,
        provider=provider,
        sort=sort,
    )

@router.get("/{job_id}")
async def get_job(
    job_id: int,
    db: Session = Depends(get_db),
):

    job = db.get(Job, job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    return job