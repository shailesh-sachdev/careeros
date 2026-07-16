import json
import re

from app.ai.manager import AIManager
from app.ai.json_utils import parse_llm_json


class InterviewQuestionGenerator:

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
    ) -> dict:

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
You are a senior engineering manager and technical interviewer.

Generate interview questions specifically for this candidate.

Rules:

- Return ONLY valid JSON.
- Never use markdown.
- Never include explanations outside JSON.
- Never invent experience.
- Base the questions on BOTH the candidate's resume and the target job.

Generate:

- 10 Technical Questions
- 5 Behavioral Questions

Return exactly this JSON:

{
  "technical": [
    {
      "question": "",
      "why_this_is_asked": "",
      "expected_answer": "",
      "difficulty": "Easy"
    }
  ],
  "behavioral": [
    {
      "question": "",
      "why_this_is_asked": "",
      "expected_answer": ""
    }
  ]
}
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

Generate interview questions.
"""

        response = await self.ai.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )
        with open(
            "interview_response.txt",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(response)
        return parse_llm_json(
            response,
        )