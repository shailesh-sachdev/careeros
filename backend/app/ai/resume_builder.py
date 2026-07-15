class ResumeBuilder:

    def build(
        self,
        profile: dict,
        summary: str,
        experiences: list[dict],
    ) -> str:

        skills = "\n".join(
            f"- {skill}"
            for skill in profile.get("skills", [])
        )

        experience_md = ""

        for experience in experiences:

            experience_md += f"""
### {experience["role"]}

**{experience["company"]}**

📅 {experience["dates"]}

{experience["details"]}

"""

        projects_md = ""

        for project in profile.get(
            "projects",
            [],
        ):

            projects_md += f"""
### {project["name"]}

{project["details"]}

"""

        education_md = ""

        for education in profile.get(
            "education",
            [],
        ):

            education_md += f"""
- **{education["degree"]}**

  {education.get("year", "")}

"""

        certifications_md = ""

        certifications = profile.get(
            "certifications",
            [],
        )

        if certifications:

            certifications_md = "\n".join(
                f"- {certification}"
                for certification in certifications
            )

        markdown = f"""# {profile["name"]}

📧 {profile["email"]}

📞 {profile["phone"]}

🔗 LinkedIn: {profile.get("linkedin", "")}

🔗 GitHub: {profile.get("github", "")}

---

# Professional Summary

{summary}

---

# Technical Skills

{skills}

---

# Professional Experience

{experience_md}

---

# Projects

{projects_md}

---

# Education

{education_md}
"""

        if certifications_md:

            markdown += f"""

---

# Certifications

{certifications_md}
"""

        return markdown.strip()