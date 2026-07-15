import json

from app.ai.manager import AIManager


class JobMatcher:

    def __init__(self):
        self.ai = AIManager()

    async def match(
        self,
        resume_text: str,
        job_title: str,
        location: str | None,
        department: str | None,
        description: str | None,
    ) -> dict:

        system_prompt = """
You are an expert technical recruiter with over 20 years of experience.

Your job is to objectively evaluate how well a candidate matches a job posting.

Return ONLY valid JSON.

{
    "match_score": 0,
    "strengths": [
        {
            "resume_evidence": "",
            "matched_requirement": ""
        }
    ],
    "missing_skills": [],
    "summary": ""
}

Evaluation Rules:

1. The match_score must be between 0 and 100.

2. The score must reflect:
   - Technical skills
   - Years of experience
   - Seniority level
   - Domain experience
   - Responsibilities
   - Required technologies
   - Leadership expectations

3. Never increase the score because the candidate is generally a good engineer.
   Only score based on evidence found in the resume.

4. For each strength:
   - Find something explicitly written in the resume.
   - Match it to a requirement from the job.
   - Do not invent experience.

5. For missing_skills:
   - List ONLY technologies, skills, responsibilities, qualifications or experience
     that are required in the job description but NOT demonstrated in the resume.
   - NEVER list skills that already appear in the resume.
   - NEVER repeat strengths.

6. If the role is significantly more senior than the candidate,
   reduce the score accordingly.

7. If the role belongs to a different specialization
   (for example ML Platform, DevOps, Data Engineering, Mobile, Security),
   reduce the score accordingly.

8. The summary must briefly explain why the score was assigned.

Return ONLY JSON.
"""

        user_prompt = f"""
Candidate Resume

-------------------------

{resume_text}

=========================

Job Title

{job_title}

Location

{location}

Department

{department}

Job Description

{description}
"""

        response = await self.ai.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return json.loads(response)