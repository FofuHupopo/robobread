from fastapi import APIRouter
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .services import ModbusService
from .utils import getenv


router = APIRouter(
    prefix="/interaction"
)

main_app_lifespan = router.lifespan_context
service = ModbusService(getenv("MODBUS_PORT"), 1)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()

    async with main_app_lifespan(app) as maybe_state:
        yield maybe_state

    await shutdown()


async def startup():
    service.connect()
    print("Modbus device connected")


async def shutdown():
    service.disconnect()
    print("Modbus device disconnected")


@router.get("/sell/{cell_number}")
async def sell_item(cell_number: int):
    service.sell_item(cell_number)
    
    return {"message": f"Item sold in cell number {cell_number}"}


@router.get("/open-door")
async def open_door():
    return {"message": f"Door opened"}


@router.get("/ping")
async def ping():
    return {"message": f"Pong"}
