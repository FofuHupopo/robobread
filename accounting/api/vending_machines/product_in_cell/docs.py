from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status

from .serializers import ProductsInCellSerializer


vending_machine_products_in_cell_list = extend_schema_view(
    get=extend_schema(
        summary="Получение списка товаров в ячеке автомата",
        description="Получение списка товаров, которые лежат в автомате. Представляют собой срок годности товара и дату отгрузки.",
        responses={
            status.HTTP_200_OK: ProductsInCellSerializer
        },
        tags=["Товары ячеек автомата"],
    ),
    put=extend_schema(
        summary="Обновление срока годности товаров в ячейке автомата",
        description="Обновление срока годности товаров в ячейке автомата. Обновляются только поля expiration_date и upload_date, остальные игнорируют изменения",
        request=ProductsInCellSerializer,
        responses={
            status.HTTP_200_OK: ProductsInCellSerializer
        },
        tags=["Товары ячеек автомата"],
    )
)
