from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repositories.url_repository import URLRepository
from app.services.url_service import URLService

def get_url_service(db: Session = Depends(get_db)) -> URLService:
    url_repo = URLRepository(db)
    return URLService(url_repo)
