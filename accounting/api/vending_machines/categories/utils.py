from api.exceptions import NoObjectException
from api.products.models import CategoryModel


def get_category_by_sku(category_sku: str) -> CategoryModel:
    try:
        category = CategoryModel.objects.get(
            sku=category_sku
        )
    except CategoryModel.DoesNotExist:
        raise NoObjectException(
            "Category not found",
            {"message": f"Category with sku=\"{category_sku}\" not found"},
        )

    return category
