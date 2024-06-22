import uvicorn
from fastapi import FastAPI, APIRouter

from app.controllers import router, lifespan
from app.utils import getenv


app = FastAPI(lifespan=lifespan)

api_router = APIRouter(
    prefix="/api"
)
api_router.include_router(router)


@app.get("/")
async def index():
    return "Interaction microservice"


def main():
    uvicorn.run(
        "main:app",
        host=getenv("HOST"),
        port=int(getenv("PORT")),
        reload=True,
        workers=int(getenv("WORKERS")) or 1
    )
