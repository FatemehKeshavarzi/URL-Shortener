from typing import List, Optional
from models.url import ShortenedURL

class URLRepository:
    def __init__(self, db):
        self.db = db

    def create(self, original_url: str, short_code: str) -> ShortenedURL:
        shortenedurl = ShortenedURL(original_url=original_url, short_code=short_code)
        self.db.add(shortenedurl)
        self.db.commit()
        self.db.refresh(shortenedurl)
        return shortenedurl
    
    def get_by_code(self, code: str) -> Optional[ShortenedURL]:
        return self.db.query(ShortenedURL).filter(ShortenedURL.short_code == code).first()
