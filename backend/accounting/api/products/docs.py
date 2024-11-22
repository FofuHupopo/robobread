from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes


category_list = extend_schema_view(
    get=extend_schema(
        summary='Получение списка категорий',
        description='Получение списка категорий',
        tags=['Категории'],
    ),
    post=extend_schema(
        summary='Создание категории',
        description='Создание категории',
        tags=['Категории'],
    ),
)

category_detail = extend_schema_view(
    get=extend_schema(
        summary='Получение категории',
        description='Получение категории',
        tags=['Категории'],
    ),
    put=extend_schema(
        summary='Обновление категории',
        description='Обновление категории',
        tags=['Категории'],
    ),
    patch=extend_schema(
        summary='Обновление категории',
        description='Обновление категории',
        tags=['Категории'],
    ),
    delete=extend_schema(
        summary='Удаление категории',
        description='Удаление категории',
        tags=['Категории'],
    )
)

product_list = extend_schema_view(
    get=extend_schema(
        summary='Получение списка товаров',
        description='Получение списка товаров',
        parameters=[
            OpenApiParameter(
                name='category_id',
                location=OpenApiParameter.QUERY,
                description='ID категории',
                type=OpenApiTypes.INT
            )
        ],
        tags=['Товары', 'Категории'],
    ),
    post=extend_schema(
        summary='Создание товара',
        description='Создание товара',
        tags=['Товары'],
    )
)

product_detail = extend_schema_view(
    get=extend_schema(
        summary='Получение товара',
        description='Получение товара',
        tags=['Товары'],
    ),
    put=extend_schema(
        summary='Обновление товара',
        description='Обновление товара',
        tags=['Товары'],
    ),
    patch=extend_schema(
        summary='Обновление товара',
        description='Обновление товара',
        tags=['Товары'],
    ),
    delete=extend_schema(
        summary='Удаление товара',
        description='Удаление товара',
        tags=['Товары'],
    )
)
