import json

from app.ai.manager import AIManager


class JobMatcher:

    def __init__(self):
        self.ai = AIManager()

    async def match(
        self,
        resume_text: str,
        job_description: str,
    ) -> dict:

        system_prompt = """
You are an expert technical recruiter.

Compare a candidate resume with a job description.

Return ONLY valid JSON.

{
    "match_score": 0,
    "strengths": [],
    "missing_skills": [],
    "summary": ""
}

Rules:

- match_score must be between 0 and 100.
- strengths must contain only matching skills or experience.
- missing_skills must contain only missing technical skills.
- summary must be under 80 words.
"""

        user_prompt = f"""
Resume:

{resume_text}

------------------------------------

Job Description:

{job_description}
"""

        response = await self.ai.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return json.loads(response)