from app.ai.manager import AIManager
import re


class SummaryOptimizer:

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
        summary: str,
        skills: list[str],
        job_title: str,
        department: str | None,
        job_description: str,
    ) -> str:

        job_description = self.clean_job_description(
            job_description,
        )

        system_prompt = """
You are a senior technical recruiter and ATS resume expert.

Your ONLY task is to rewrite ONE professional summary.

Rules:

- Return ONLY the rewritten summary.
- Never invent technologies.
- Never invent experience.
- Never invent certifications.
- Never invent achievements.
- Never change years of experience.
- Never exaggerate.
- Use ONLY information supplied.
- Optimize for ATS.
- Prioritize skills relevant to the job.
- Keep it between 3 and 5 sentences.
"""

        user_prompt = f"""
Candidate Summary

{summary}

==================================================

Candidate Skills

{", ".join(skills)}

==================================================

Target Job

Title:
{job_title}

Department:
{department if department else "Not specified"}

Description:

{job_description}

==================================================

Rewrite ONLY the professional summary.
"""

        response = await self.ai.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return (
            response
            .replace("```", "")
            .replace("markdown", "")
            .strip()
        )