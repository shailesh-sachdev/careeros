from typing import Any

from app.models.job import Job


class JobNormalizer:

    @staticmethod
    def normalize_greenhouse(job: dict[str, Any]) -> dict:

        departments = ", ".join(
            department["name"]
            for department in job.get("departments", [])
        ) or None

        offices = ", ".join(
            office["name"]
            for office in job.get("offices", [])
        ) or None

        return {
            "provider": "greenhouse",
            "provider_job_id": str(job["id"]),
            "title": job.get("title"),
            "company_name": job.get("company_name"),
            "company_website": None,
            "location": job.get("location", {}).get("name"),
            "description": job.get("content"),
            "employment_type": None,
            "job_url": job.get("absolute_url"),
            "posted_at": job.get("updated_at"),
            "department": departments,
            "team": offices,
            "requirements": None,
            "responsibilities": None,
            "benefits": None,
        }