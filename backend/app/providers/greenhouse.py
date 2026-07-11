import httpx

from app.providers.base import BaseProvider
from app.schemas.job_import import JobImport


class GreenhouseProvider(BaseProvider):

    BASE_URL = "https://boards-api.greenhouse.io/v1/boards"

    async def fetch_jobs(
        self,
        board_token: str,
    ) -> list[JobImport]:

        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.get(
                f"{self.BASE_URL}/{board_token}/jobs"
            )

            response.raise_for_status()

            data = response.json()

        jobs = []

        for item in data["jobs"]:

            jobs.append(
                JobImport(
                    provider="greenhouse",
                    provider_job_id=str(item["id"]),
                    title=item["title"],
                    company_name=board_token.replace("-", " ").title(),
                    company_website=None,
                    location=item.get("location", {}).get("name"),
                    description=None,
                    employment_type=None,
                    job_url=item["absolute_url"],
                    posted_at=item.get("updated_at"),
                )
            )

        return jobs