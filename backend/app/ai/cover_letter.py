import json
import re

from app.ai.manager import AIManager


class CoverLetterGenerator:

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

        return description[:4000]

    async def generate(
        self,
        resume_json: dict | str,
        job_title: str,
        department: str | None,
        job_description: str,
    ) -> str:

        if isinstance(
            resume_json,
            str,
        ):
            resume = json.loads(
                resume_json,
            )
        else:
            resume = resume_json

        job_description = self.clean_job_description(
            job_description,
        )

        system_prompt = """
You are an expert technical recruiter and professional career coach.

Write a professional cover letter.

Rules:

- Be truthful.
- Never invent experience.
- Never invent projects.
- Never invent companies.
- Never invent achievements.
- Never exaggerate.

Requirements:

- Address the hiring team professionally.
- Explain why the candidate is interested.
- Highlight the most relevant experience.
- Mention relevant projects.
- Mention relevant technical skills.
- Show enthusiasm.
- End with a professional closing.

Length:

300-450 words.

Return ONLY the cover letter.

Do not use markdown.

Do not use code fences.
"""

        user_prompt = f"""
Candidate

{json.dumps(resume, indent=2)}

==================================================

Target Job

Title:
{job_title}

Department:
{department if department else "Not specified"}

Description:

{job_description}

==================================================

Write a tailored professional cover letter.
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