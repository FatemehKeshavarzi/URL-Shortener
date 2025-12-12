from fastapi import FastAPI
import uvicorn
from app.api.routers import url_router


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
