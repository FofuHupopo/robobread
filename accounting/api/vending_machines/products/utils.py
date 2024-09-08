from api.exceptions import NoObjectException
from api.products.models import ProductModel


def get_product_by_sku(product_sku: str) -> ProductModel:
    try:
        product = ProductModel.objects.get(
            sku=product_sku
        )
    except ProductModel.DoesNotExist:
        raise NoObjectException(
            "Product not found",
            {"message": f"Product with sku=\"{product_sku}\" not found"},
        )

    return product
