from django.urls import path

from . import views


app_name = 'products'

urlpatterns = [
    path('category', views.CategoryListView.as_view(), name="category_list"),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name="category_detail"),

    path('category/<int:category_id>/product', views.ProductListView.as_view(), name="category_detail"),

    path('product', views.ProductListView.as_view(), name="product_list"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
]
