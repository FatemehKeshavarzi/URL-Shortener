from repositories.url_repository import URLRepository
from models.url import ShortenedURL



class URLService:
    def __init__(self, url_repo: URLRepository):
        self.url_repo = url_repo

    
    def get_by_code(self, code: str) -> str:
        link = self.url_repo.get_by_code(code)
        if not link:
            raise ValueError(f"There is no such a link named ({link}) . please try another code")
        return link.original_url