from pathlib import Path


def load_resume_template() -> str:

    path = (
        Path(__file__)
        .parent
        / "resume_template.md"
    )

    return path.read_text(
        encoding="utf-8",
    )