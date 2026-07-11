from fastapi import APIRouter

from app.providers.greenhouse import GreenhouseProvider

router = APIRouter(prefix="/providers")


@router.get("/greenhouse/{board}")
async def greenhouse_jobs(board: str):

    provider = GreenhouseProvider()

    jobs = await provider.fetch_jobs(board)

    return jobs