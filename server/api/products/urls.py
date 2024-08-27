from django.urls import path

from . import views


urlpatterns = [
    path("category", views.CategoryListAPIView.as_view(), name="products__category_list"),
    path("category/<int:pk>", views.CategoryDetailAPIView.as_view(), name="products__category_deyail"),

    path("all-product", views.AllProductListAPIView.as_view(), name="products__all_product_list"),
    
    path("product", views.ProductListAPIView.as_view(), name="products__product_list"),
    path("product/<int:pk>", views.ProductDetailAPIView.as_view(), name="products__product_deyail"),

    path("cell", views.CellListAPIView.as_view(), name="products__cell_list"),
    path("cell/<int:pk>", views.CellDetailAPIView.as_view(), name="products__cell_deyail"),

    path("cell/<int:cell>/products", views.ProductInCellView.as_view(), name="products__products_in_cell"),
    path("cell/<int:cell>/products/<int:pk>", views.ProductInCellDetailView.as_view(), name="products__products_in_cell_detail"),
]
