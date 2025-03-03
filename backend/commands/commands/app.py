from fastapi import FastAPI, APIRouter
from .controllers import router


app = FastAPI(
    title="Commands API",
    description="API для получения команд торгового автомата",
    version="1.0.0",
)

app.include_router(router)

@app.get("/")
async def index():
    return "Commands Microservice"
