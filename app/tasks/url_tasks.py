from app.db.session import get_db
from app.services.url_service import URLService
from app.repositories.url_repository import URLRepository


def delete_expired_urls() -> None:
    db = next(get_db())
    url_service = URLService(url_repo=URLRepository(db=db))
    url_service.delete_expired_urls()