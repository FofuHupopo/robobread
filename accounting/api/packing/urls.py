from django.urls import path

from . import views


app_name = 'packing'

urlpatterns = [
    path("packing", views.PackingView.as_view(), name="packing_list"),
    path("packing/<int:pk>", views.PackingDetailView.as_view(), name="packing_detail")
]
