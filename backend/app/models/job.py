from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UniqueConstraint
from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"
    __table_args__ = (
    UniqueConstraint(
            "provider",
            "provider_job_id",
            name="uq_provider_job",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
    )
    provider: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    provider_job_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    applications: Mapped[list["Application"]] = relationship(
        back_populates="job",
        cascade="all, delete-orphan",
    )

    title: Mapped[str] = mapped_column(String(255), nullable=False)

    location: Mapped[str | None] = mapped_column(String(255), nullable=True)

    employment_type: Mapped[str | None] = mapped_column(String(100), nullable=True)

    job_url: Mapped[str] = mapped_column(String(1000), nullable=False, unique=True)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # source: Mapped[str] = mapped_column(String(50), nullable=False)

    posted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    company: Mapped["Company"] = relationship(back_populates="jobs")