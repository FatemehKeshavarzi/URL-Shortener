from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.sql import func
from url_shortener.models.base import Base  # Import the base SQLAlchemy model


# Name of the table in the database
TABLE_NAME = "shortened_urls"


class ShortenedURL(Base):
    """
    SQLAlchemy model for storing shortened URL data.
    """
    __tablename__ = TABLE_NAME

    # Primary key (id)
    id = Column(Integer, primary_key=True, index=True)

    # Original URL (can be long, must not be null)
    original_url = Column(String, nullable=False)

    # Shortened code (must be UNIQUE and indexed)
    # VARCHAR(10)
    short_code = Column(String(10), unique=True, nullable=False)

    # Creation timestamp
    # func.now() automatically sets the timestamp when the record is created
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Optional: expiration time (TTL support)
    expires_at = Column(DateTime, nullable=True)

    # Explicit index on short_code for fast lookup of GET /u/{short_code}
    __table_args__ = (
        Index("idx_short_code", short_code),
    )

    def __repr__(self):
        """Readable object representation for debugging."""
        return f"<ShortenedURL(short_code='{self.short_code}', original_url='{self.original_url}')>"
