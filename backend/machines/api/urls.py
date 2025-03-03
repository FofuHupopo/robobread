from django.urls import path, include

urlpatterns = [
    path("synchronizer/", include("api.synchronizer.urls")),
]
