from fastapi import Depends
from sqlalchemy.orm import Session
from db.session import get_db
from repositories.url_repository import URLRepository
from services.url_service import URLService

def get_url_service(db: Session = Depends(get_db)) -> URLService:
    url_repo = URLRepository(db)
    return URLService(url_repo)
