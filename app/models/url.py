from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Index
from app.models.base import Base 


class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String(10), unique=True, nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    expires_at = Column(DateTime, nullable=True)

    __table_args__ = (
        Index("idx_short_code", short_code),
    )

    def __repr__(self):
        return f"<ShortenedURL(short_code='{self.short_code}', original_url='{self.original_url}')>"
