from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base 


class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id : Mapped[int]  = mapped_column(Integer, primary_key=True, index=True)
    original_url : Mapped[str] = mapped_column(String, nullable=False)
    short_code : Mapped[str | None] = mapped_column(String(10), unique=True, nullable=True, index=True)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    expires_at : Mapped[datetime|None] = mapped_column(DateTime, nullable=True)

    def __repr__(self):
        return f"<ShortenedURL(short_code='{self.short_code}', original_url='{self.original_url}')>"
