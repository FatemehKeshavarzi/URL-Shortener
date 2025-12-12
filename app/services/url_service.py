from typing import Sequence
from app.repositories.url_repository import URLRepository
from app.models.url import ShortenedURL
from app.utils.short_code_generator import encode_base62



class URLService:
    def __init__(self, url_repo: URLRepository):
        self.url_repo = url_repo

    def create(self, original_url: str) -> ShortenedURL:
        existing = self.url_repo.get_by_origonal_url(original_url)
        if existing:
            raise ValueError(f"There is a link named ({original_url}) . please try another link.")
        
        new_url = ShortenedURL(original_url=original_url)
        self.url_repo.add(new_url)
        self.url_repo.flush()  

        short_code = encode_base62(new_url.id)
        addable_url = new_url.id
        while self.url_repo.get_by_code(short_code):
            addable_url += 1
            short_code = encode_base62(addable_url)

        new_url.short_code = short_code

        self.url_repo.commit()
        return new_url
    
    def get_by_code(self, code: str) -> ShortenedURL:
        link = self.url_repo.get_by_code(code)
        if not link:
            raise ValueError(f"There is no such a shortened_link named ({code}) . please try another code")
        return link
    
    def list_urls(self) -> Sequence[ShortenedURL]:
        return self.url_repo.all()

    def delete_by_code(self, code:str) -> None:
        url = self.url_repo.get_by_code(code=code)
        if not url:
            raise ValueError("url not found")
        self.url_repo.delete_by_code(url=url)