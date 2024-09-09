from django.urls import path

from . import views


urlpatterns = [
    path("category", views.CategoryListView.as_view(), name="products__category_list"),
    path("category/<int:pk>", views.CategoryDetailView.as_view(), name="products__category_deyail"),

    path("all-product", views.AllProductListView.as_view(), name="products__all_product_list"),
    path("all-product/<int:pk>", views.ProductDetailView.as_view(), name="products__all_product_deyail"),

    path("product", views.ProductListView.as_view(), name="products__product_list"),

    path("cell", views.CellListView.as_view(), name="products__cell_list"),
    path("cell/<int:pk>", views.CellDetailView.as_view(), name="products__cell_deyail"),

    path("cell/<int:cell>/products", views.ProductInCellView.as_view(), name="products__products_in_cell"),
    path("cell/<int:cell>/products/<int:pk>", views.ProductInCellDetailView.as_view(), name="products__products_in_cell_detail"),

    path("packing", views.PackingView.as_view(), name="products__packing"),
]
