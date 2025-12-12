from typing import List, Optional
from app.models.url import ShortenedURL

class URLRepository:
    def __init__(self, db):
        self.db = db

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
