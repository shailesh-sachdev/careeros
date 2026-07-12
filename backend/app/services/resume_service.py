import shutil
import uuid
from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.services.text_extraction_service import TextExtractionService


UPLOAD_DIR = Path("uploads/resumes")


class ResumeService:

    def upload(
        self,
        db: Session,
        candidate_profile_id: int,
        file: UploadFile,
    ) -> Resume:

        UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        extension = Path(file.filename).suffix

        filename = f"{uuid.uuid4()}{extension}"

        destination = UPLOAD_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        extractor = TextExtractionService()

        raw_text = extractor.extract(
            str(destination),
        )

        resume = Resume(
            candidate_profile_id=candidate_profile_id,
            filename=filename,
            original_filename=file.filename,
            file_path=str(destination),
            mime_type=file.content_type,
            file_size=destination.stat().st_size,
            raw_text=raw_text,
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return resume