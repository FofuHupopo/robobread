from django.urls import path

from . import views


urlpatterns = [
    path("category", views.CategoryListAPIView.as_view(), name="products__category_list"),
    path("category/<int:pk>", views.CategoryDetailAPIView.as_view(), name="products__category_deyail"),
    
    path("product", views.ProductListAPIView.as_view(), name="products__product_list"),
    path("product/<int:pk>", views.ProductDetailAPIView.as_view(), name="products__product_deyail"),
]
