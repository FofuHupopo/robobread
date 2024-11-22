from typing import List

from fastapi import APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from ...config import settings
from ...gateway import route

from . import models


router = APIRouter()

SERVICE_URL = settings.ACCOUNTING_SERVICE_URL

print(SERVICE_URL)


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/vending-machines/sync",
    service_path="/vending-machines/sync",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=List[models.VendingMachineSync],
    tags=["Учет.Синхронизация"],
)
async def vending_machines_sync_all(request: Request, response: Response):
    pass


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/vending-machines/{vending_machine_id}/sync",
    service_path="/vending-machines/vending-machine/{vending_machine_id}/sync",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=models.VendingMachineSync,
    tags=["Учет.Синхронизация"],
)
async def vending_machines_sync_one(vending_machine_id: int, request: Request, response: Response):
    pass
