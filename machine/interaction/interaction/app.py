from fastapi import FastAPI, APIRouter

from .controllers import router, lifespan


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
