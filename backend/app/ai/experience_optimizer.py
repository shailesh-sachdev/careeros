import re

from app.ai.manager import AIManager


class ExperienceOptimizer:

    def __init__(self):
        self.ai = AIManager()

    def clean_job_description(
        self,
        description: str | None,
    ) -> str:

        if not description:
            return ""

        description = re.sub(
            r"<[^>]+>",
            " ",
            description,
        )

        description = (
            description
            .replace("&nbsp;", " ")
            .replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&#39;", "'")
            .replace("&quot;", '"')
        )

        description = re.sub(
            r"\s+",
            " ",
            description,
        )

        return description[:2000]

    async def optimize(
        self,
        company: str,
        role: str,
        dates: str,
        details: str,
        job_title: str,
        department: str | None,
        job_description: str,
    ) -> dict:

        job_description = self.clean_job_description(
            job_description,
        )

        system_prompt = """
You are a senior technical recruiter and ATS optimization expert.

Your ONLY task is to rewrite ONE work experience.

Rules:

- Return ONLY valid JSON.
- Never invent companies.
- Never invent dates.
- Never invent technologies.
- Never invent achievements.
- Never invent responsibilities.
- Never exaggerate.
- Preserve all facts.
- Rewrite the wording to better align with the target job.
- Highlight the most relevant backend, API, automation and engineering work if it already exists.

Return exactly this JSON:

{
    "company": "",
    "role": "",
    "dates": "",
    "details": ""
}
"""

        user_prompt = f"""
Experience

Company:
{company}

Role:
{role}

Dates:
{dates}

Details:
{details}

==================================================

Target Job

Title:
{job_title}

Department:
{department if department else "Not specified"}

Description:

{job_description}

==================================================

Rewrite ONLY this experience.

Do not change company.

Do not change role.

Do not change dates.

Only improve the wording of the details.
"""

        response = await self.ai.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        import json

        return json.loads(response)