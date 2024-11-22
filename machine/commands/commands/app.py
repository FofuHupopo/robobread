from fastapi import FastAPI, APIRouter
from .controllers import router


app = FastAPI(
    title="Commands API",
    description="API для команд для торгового автомата",
    version="1.0.0",
)

api_router = APIRouter(
    prefix="/api"
)
api_router.include_router(router)

app.include_router(api_router)


@app.get("/")
async def index():
    return "Commands Microservice"
