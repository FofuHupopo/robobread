from fastapi import APIRouter
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .services import MDBService
from .utils import getenv


router = APIRouter(
    prefix="/terminal"
)

main_app_lifespan = router.lifespan_context
service = MDBService(getenv("MDB_PORT"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()

    async with main_app_lifespan(app) as maybe_state:
        yield maybe_state

    await shutdown()


async def startup():
    service.connect()
    print("MDB device connected")


async def shutdown():
    service.disconnect()
    print("MDB device disconnected")


@router.get("/ping")
async def ping():
    return {"message": f"Pong"}
