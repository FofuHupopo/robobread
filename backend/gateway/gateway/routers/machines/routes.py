from typing import List

from fastapi import APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from ...config import settings
from ...gateway import route

from . import models


router = APIRouter()

SERVICE_URL = settings.MACHINES_SERVICE_URL
