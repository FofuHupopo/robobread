from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import services
from api.vending_machines.models import VendingMachineModel
from . import serializers


class CategoryListView(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if "category_id" not in self.kwargs:
            return queryset
        
        category_id = self.kwargs["category_id"]
        
        return queryset.filter(
            category_id=category_id
        )


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


class VendingMachineCategoryListView(APIView):
    serializer_class = serializers.CategoryDataSerializer
    service_class = services.CategoryService

    def get(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(
            self.service_class(vending_machine).sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def post(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        category_sku = request.data.get("category_sku")

        try:
            category = models.CategoryModel.objects.get(
                sku=category_sku
            )
        except models.CategoryModel.DoesNotExist:
            return Response(
                {"message": "Category not found"},
                status.HTTP_404_NOT_FOUND
            )

        service = self.service_class(vending_machine)
        service.create_category(category)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
    
    def delete(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        category_sku = request.data.get("category_sku")

        try:
            category = models.CategoryModel.objects.get(
                sku=category_sku
            )
        except models.CategoryModel.DoesNotExist:
            return Response(
                {"message": "Category not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        service = self.service_class(vending_machine)
        service.delete_category(category)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def put(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        category_sku = request.data.get("category_sku")

        try:
            category = models.CategoryModel.objects.get(
                sku=category_sku
            )
        except models.CategoryModel.DoesNotExist:
            return Response(
                {"message": "Category not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        service = self.service_class(vending_machine)
        service.update_category(category)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


class VendingMachineProductListView(APIView):
    serializer_class = serializers.ProductDataSerializer
    service_class = services.ProductService

    def get(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(
            self.service_class(vending_machine).sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def post(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        product_sku = request.data.get("product_sku")

        try:
            product = models.ProductModel.objects.get(
                sku=product_sku
            )
        except models.ProductModel.DoesNotExist:
            return Response(
                {"message": "Product not found"},
                status.HTTP_404_NOT_FOUND
            )

        service = self.service_class(vending_machine)
        service.create_product(product)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
    
    def delete(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        product_sku = request.data.get("product_sku")

        try:
            product = models.ProductModel.objects.get(
                sku=product_sku
            )
        except models.ProductModel.DoesNotExist:
            return Response(
                {"message": "Product not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        service = self.service_class(vending_machine)
        service.delete_product(product)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def put(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = VendingMachineModel.objects.get(
                pk=vending_machine_id
            )
        except VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        product_sku = request.data.get("product_sku")

        try:
            product = models.ProductModel.objects.get(
                sku=product_sku
            )
        except models.ProductModel.DoesNotExist:
            return Response(
                {"message": "Product not found"},
                status.HTTP_404_NOT_FOUND
            )
        
        service = self.service_class(vending_machine)
        service.update_product(product)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
