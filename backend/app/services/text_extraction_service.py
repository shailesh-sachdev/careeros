from pathlib import Path

import fitz
from docx import Document


class TextExtractionService:

    def extract(self, file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return self._extract_pdf(file_path)

        if extension == ".docx":
            return self._extract_docx(file_path)

        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    def _extract_pdf(
        self,
        file_path: str,
    ) -> str:

        document = fitz.open(file_path)

        text = []

        for page in document:
            text.append(page.get_text())

        document.close()

        return "\n".join(text)

    def _extract_docx(
        self,
        file_path: str,
    ) -> str:

        document = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )