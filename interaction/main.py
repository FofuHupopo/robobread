import uvicorn
from fastapi import FastAPI, APIRouter

from app.controllers import router, lifespan
from app.utils import getenv


app = FastAPI(
    lifespan=lifespan,
    title="Interaction API",
    description="API для сервиса взаимодействий с контроллером торгового автомата",
    version="1.0.0",
)

api_router = APIRouter(
    prefix="/api"
)
api_router.include_router(router)

app.include_router(api_router)


@app.get("/")
async def index():
    return "Interaction Microservice"


def main():
    uvicorn.run(
        "main:app",
        host=getenv("HOST"),
        port=int(getenv("PORT")),
        reload=True,
        workers=int(getenv("WORKERS")) or 1
    )


if __name__ == "__main__":
    main()
