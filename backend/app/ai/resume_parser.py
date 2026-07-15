import json

from app.ai.manager import AIManager


class ResumeParser:

    def __init__(self):
        self.ai = AIManager()

    async def parse(
        self,
        raw_text: str,
    ) -> str:

        system_prompt = """
You are an expert resume parser.

Return ONLY valid JSON.

Do not include markdown.

Do not explain anything.

Return this exact structure:

{
  "name": "",
  "email": "",
  "phone": "",
  "linkedin": "",
  "github": "",
  "summary": "",
  "skills": [],
  "experience": [],
  "education": [],
  "projects": [],
  "certifications": []
}
"""

        response = await self.ai.generate(
            system_prompt=system_prompt,
            user_prompt=raw_text,
        )

        print("=" * 80)
        print(response)
        print("=" * 80)

        return response