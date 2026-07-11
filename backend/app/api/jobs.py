from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.services.job_query_service import JobQueryService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get("")
async def list_jobs(
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
    db: Session = Depends(get_db),
):

    service = JobQueryService()

    return service.list_jobs(
        db=db,
        page=page,
        page_size=page_size,
    )