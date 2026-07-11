from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.application import ApplicationStatus
from app.services.application_service import ApplicationService
from app.models.application import Application

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.post("/{job_id}")
async def create_application(
    job_id: int,
    db: Session = Depends(get_db),
):

    service = ApplicationService()

    return service.create(
        db=db,
        job_id=job_id,
    )


@router.patch("/{application_id}")
async def update_application(
    application_id: int,
    status: ApplicationStatus,
    db: Session = Depends(get_db),
):

    service = ApplicationService()

    application = service.get(
        db=db,
        application_id=application_id,
    )

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found",
        )

    return service.update_status(
        db=db,
        application=application,
        status=status,
    )

@router.get("")
async def list_applications(
    db: Session = Depends(get_db),
):

    return db.query(Application).all()