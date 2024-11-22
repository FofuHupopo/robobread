from typing import List

from fastapi import APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from ...config import settings
from ...gateway import route

from . import models


router = APIRouter()

SERVICE_URL = settings.ANALYTICS_SERVICE_URL

print(SERVICE_URL)


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/statistics/sales/by-category",
    service_path="/statistics/sales/by-category",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=models.StatisticsSalesByCategory,
    tags=["Аналитика.Статистика продаж"],
)
async def statistics_sales_by_category(request: Request, response: Response): ...


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/statistics/sales/by-product",
    service_path="/statistics/sales/by-product",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=models.StatisticsSalesByProduct,
    tags=["Аналитика.Статистика продаж"],
)
async def statistics_sales_by_product(request: Request, response: Response): ...


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/statistics/sales/percent-of-redemption",
    service_path="/statistics/sales/percent-of-redemption",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=models.StatisticsSalesPercentOfRedemption,
    tags=["Аналитика.Статистика продаж"],
)
async def statistics_sales_percent_of_redemption(request: Request, response: Response): ...


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/statistics/sales/revenue",
    service_path="/statistics/sales/revenue",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=models.StatisticsSalesRevenue,
    tags=["Аналитика.Статистика продаж"],
)
async def statistics_sales_revenue(request: Request, response: Response): ...


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/statistics/sales/revenue-for-the-week",
    service_path="/statistics/sales/revenue-for-the-week",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=models.StatisticsSalesRevenueForTheWeek,
    tags=["Аналитика.Статистика продаж"],
)
async def statistics_sales_revenue_for_the_week(request: Request, response: Response): ...


@route(
    request_method=router.get,
    service_url=SERVICE_URL,
    gateway_path="/statistics/product-stock/all",
    service_path="/statistics/product-stock/all",
    status_code=status.HTTP_200_OK,
    override_headers=False,
    response_model=List[models.StatisticsProductStockAll],
    tags=["Аналитика.Товарный остаток"],
)
async def statistics_product_stock_all(request: Request, response: Response): ...
