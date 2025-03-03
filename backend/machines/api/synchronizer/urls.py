from django.urls import path

from . import views

urlpatterns = [
    path('register-machine', views.RegisterMachineView.as_view(), name='register_machine'),

    path('machine-order', views.MachineOrderView.as_view(), name='machine_order'),
    path('machine-order/<str:key>', views.MachineOrderView.as_view(), name='machine_order'),

    path('machine-category', views.MachineCategoryView.as_view(), name='machine_category'),
    path('machine-category/<str:key>', views.MachineCategoryView.as_view(), name='machine_category'),

    path('machine-product', views.MachineProductView.as_view(), name='machine_product'),
    path('machine-product/<str:key>', views.MachineProductView.as_view(), name='machine_product'),

    path('machine-cell', views.MachineCellView.as_view(), name='machine_cell'),
    path('machine-cell/<str:key>', views.MachineCellView.as_view(), name='machine_cell'),

    path('machine-product-in-cell', views.MachineProductInCellView.as_view(), name='machine_product_in_cell'),
    path('machine-product-in-cell/<str:key>', views.MachineProductInCellView.as_view(), name='machine_product_in_cell'),
]
