from fastapi import FastAPI
import uvicorn
from app.api import url_router
from app.repositories.url_repository import URLRepository
from app.db.session import SessionLocal

app = FastAPI(
    title="URL Shortener",
    description="Web API format",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(url_router.router)

if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)

# @app.on_event("startup")
# async def startup_event():
#     db = SessionLocal()
#     url_repo = URLRepository(db)
#     print("Application startup complete")