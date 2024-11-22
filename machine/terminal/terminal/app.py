from fastapi import FastAPI, APIRouter

from .controllers import router, lifespan


app = FastAPI(lifespan=lifespan)

api_router = APIRouter(
    prefix="/api"
)
api_router.include_router(router)

app.include_router(api_router)


@app.get("/")
async def index():
    return "Terminal microservice"
