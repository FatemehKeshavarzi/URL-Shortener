from datetime import datetime
from typing import List, Optional, Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.url import ShortenedURL

class URLRepository:
    def __init__(self, db):
        self.db : Session = db

    def add(self, obj):
        self.db.add(obj)

    def flush(self):
        self.db.flush()

    def commit(self):
        self.db.commit()

    def refresh(self, obj):
        self.db.refresh(obj)
    
    def get_by_code(self, code: str) -> Optional[ShortenedURL]:
        return self.db.query(ShortenedURL).filter(ShortenedURL.short_code == code).first()
    
    def get_by_origonal_url(self, origonal_url: str) -> Optional[ShortenedURL]:
        return self.db.query(ShortenedURL).filter(ShortenedURL.original_url == origonal_url).first()

    def all(self) -> Sequence[ShortenedURL]:
        stmt = select(ShortenedURL)
        return self.db.scalars(stmt).all()
    
    def delete(self, url:ShortenedURL) -> None:
        self.db.delete(url)
        self.commit()

    def filter(self, expired_at__lt:datetime) -> Sequence[ShortenedURL]:
        stmt = select(ShortenedURL).where(ShortenedURL.expires_at < expired_at__lt)
        return self.db.scalars(stmt).all()