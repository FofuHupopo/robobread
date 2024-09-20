from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import status

from . import serializers


category_list = extend_schema_view(
    get=extend_schema(
        summary="Список категорий",
        description="Получение списка категорий",
        tags=["Категории"],
    ),
    post=extend_schema(
        summary="Создание категории",
        description="Создание категории",
        tags=["Категории"],
    )
)

category_detail = extend_schema_view(
    get=extend_schema(
        summary="Информация о категории",
        description="Получение детальной информации по id категории",
        tags=["Категории"],
    ),
    put=extend_schema(
        summary="Изменение категории",
        description="Изменение информации категории по id",
        tags=["Категории"],
    ),
    patch=extend_schema(
        summary="Изменение категории",
        description="Изменение информации категории по id",
        tags=["Категории"],
    ),
    delete=extend_schema(
        summary="Удаление категории",
        description="Удаление категории по id",
        tags=["Категории"],
    ),
)

product_list = extend_schema_view(
    get=extend_schema(
        summary="Список товаров по категориям",
        description="Если указать category_id в query параметрах, то вернет только товары этой категории",
        parameters=[
            OpenApiParameter(
                name="category_id",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                required=False
            ),
        ],
        tags=["Товары"],
    )
)

all_product_list = extend_schema_view(
    get=extend_schema(
        summary="Список всех товаров",
        description="Получение списка всех товаров",
        tags=["Товары"],
    ),
    post=extend_schema(
        summary="Создание товара",
        description="Создание товара",
        tags=["Товары"],
    )
)

product_detail = extend_schema_view(
    get=extend_schema(
        summary="Информация о товаре",
        description="Получение детальной информации по id товара",
        tags=["Товары"],
    ),
    put=extend_schema(
        summary="Изменение товара",
        description="Изменение информации о товаре по id",
        tags=["Товары"],
    ),
    patch=extend_schema(
        summary="Изменение товара",
        description="Изменение информации о товаре по id",
        tags=["Товары"],
    ),
    delete=extend_schema(
        summary="Удаление товара",
        description="Удаление товара по id",
        tags=["Товары"],
    ),
)

cell_list = extend_schema_view(
    get=extend_schema(
        summary="Список ячеек",
        description="Получение списка ячеек",
        tags=["Ячейки"],
    ),
    post=extend_schema(
        summary="Создание ячейки",
        description="Создание ячейки",
        tags=["Ячейки"],
    )
)

cell_detail = extend_schema_view(
    get=extend_schema(
        summary="Информация о ячейке",
        description="Получение детальной информации по id ячейки",
        tags=["Ячейки"],
    ),
    put=extend_schema(
        summary="Изменение ячейки",
        description="Изменение информации ячейки по id",
        tags=["Ячейки"],
    ),
    patch=extend_schema(
        summary="Изменение ячейки",
        description="Изменение информации ячейки по id",
        tags=["Ячейки"],
    ),
    delete=extend_schema(
        summary="Удаление ячейки",
        description="Удаление ячейки по id",
        tags=["Ячейки"],
    ),
)

product_in_cell = extend_schema_view(
    get=extend_schema(
        summary="Список товаров в ячейке",
        description="Получение списка товаров в ячейке",
        tags=["Товар в ячейке"],
    ),
    post=extend_schema(
        summary="Добавление товара в ячейку",
        description="Добавление товара в ячейку",
        tags=["Товар в ячейке"],
    )
)

product_in_cell_detail = extend_schema_view(
    get=extend_schema(
        summary="Информация о товаре в ячейке",
        description="Получение детальной информации о товаре в ячейке",
        tags=["Товар в ячейке"],
    ),
    put=extend_schema(
        summary="Изменение товаре в ячейке",
        description="Изменение информации о товаре в ячейке",
        tags=["Товар в ячейке"],
    ),
    delete=extend_schema(
        summary="Удаление товара из ячейки",
        description="Удаление товара из ячейки",
        tags=["Товар в ячейке"],
    )
)

packing = extend_schema_view(
    post=extend_schema(
        summary="Затаривание",
        description="Создание нового затаривания",
        request=serializers.PackingSerializer(many=True),
        responses={
            status.HTTP_201_CREATED: serializers.PackingResultSerializer
        },
        tags=["Затаривание"]
    )
)
