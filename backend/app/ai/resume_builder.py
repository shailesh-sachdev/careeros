class ResumeBuilder:

    def build(
        self,
        profile: dict,
        summary: str,
        experiences: list[dict],
    ) -> str:

        # -----------------------------
        # Skills
        # -----------------------------

        skills = "\n".join(
            f"- {skill}"
            for skill in profile.get("skills", [])
        )

        # -----------------------------
        # Experience
        # -----------------------------

        experience_md = ""

        for experience in experiences:

            details = experience.get("details", "")

            if isinstance(details, dict):
                details = details.get(
                    "description",
                    "",
                )

            experience_md += f"""
### {experience.get("role", "")}

**{experience.get("company", "")}**

📅 {experience.get("dates", "")}

{details}

"""

        # -----------------------------
        # Projects
        # -----------------------------

        projects_md = ""

        for project in profile.get(
            "projects",
            [],
        ):

            title = (
                project.get("title")
                or project.get("name")
                or "Untitled Project"
            )

            body = []

            if project.get("details"):
                body.append(
                    project["details"]
                )

            if project.get("purpose"):
                body.append(
                    f"Purpose: {project['purpose']}"
                )

            if project.get("technologies"):
                body.append(
                    "Technologies: "
                    + ", ".join(
                        project["technologies"]
                    )
                )

            if project.get("technology"):
                body.append(
                    "Technologies: "
                    + ", ".join(
                        project["technology"]
                    )
                )

            if project.get("capabilities"):
                body.append(
                    "Capabilities: "
                    + ", ".join(
                        project["capabilities"]
                    )
                )

            projects_md += f"""
### {title}

{"\n".join(body)}

"""

        # -----------------------------
        # Education
        # -----------------------------

        education_md = ""

        for education in profile.get(
            "education",
            [],
        ):

            dates = (
                education.get("dates")
                or education.get("year")
                or ""
            )

            education_md += f"""
- **{education.get("degree", "")}**

  {dates}

"""

        # -----------------------------
        # Certifications
        # -----------------------------

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

        # -----------------------------
        # Resume
        # -----------------------------

        markdown = f"""# {profile.get("name", "")}

📧 {profile.get("email", "")}

📞 {profile.get("phone", "")}

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