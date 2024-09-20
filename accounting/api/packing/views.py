from rest_framework import generics

from . import models
from . import serializers
from . import docs


@docs.packing
class PackingView(generics.ListCreateAPIView):
    queryset = models.PackingModel.objects.all()
    serializer_class = serializers.PackingSerializer


@docs.packing_detail
class PackingDetailView(generics.RetrieveDestroyAPIView):
    queryset = models.PackingModel.objects.all()
    serializer_class = serializers.PackingSerializer
