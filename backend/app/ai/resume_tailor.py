import json

from app.ai.experience_optimizer import ExperienceOptimizer
from app.ai.resume_builder import ResumeBuilder
from app.ai.summary_optimizer import SummaryOptimizer


class ResumeTailor:

    def __init__(self):

        self.summary_optimizer = SummaryOptimizer()

        self.experience_optimizer = ExperienceOptimizer()

        self.builder = ResumeBuilder()

    async def tailor(
        self,
        resume_json: str,
        job_title: str,
        department: str | None,
        job_description: str,
    ) -> str:

        if isinstance(resume_json, str):
            profile = json.loads(resume_json)
        else:
            profile = resume_json

        summary = await self.summary_optimizer.optimize(
            summary=profile.get(
                "summary",
                "",
            ),
            skills=profile.get(
                "skills",
                [],
            ),
            job_title=job_title,
            department=department,
            job_description=job_description,
        )

        optimized_experiences = []

        for experience in profile.get(
            "experience",
            [],
        ):

            optimized = await self.experience_optimizer.optimize(
                company=experience.get(
                    "company",
                    "",
                ),
                role=experience.get(
                    "role",
                    "",
                ),
                dates=experience.get(
                    "dates",
                    "",
                ),
                details=experience.get(
                    "details",
                    "",
                ),
                job_title=job_title,
                department=department,
                job_description=job_description,
            )

            optimized_experiences.append(
                optimized,
            )

        return self.builder.build(
            profile=profile,
            summary=summary,
            experiences=optimized_experiences,
        )