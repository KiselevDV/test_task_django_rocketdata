from django.db.models import Avg

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from init.models import Address, Product, SupplyChainNode, Employee
from init.api.permissions import IsActiveEmployee
from init.api.serializers import (
    AddressSerializer, ProductSerializer, SupplyChainNodeSerializer, EmployeeSerializer)



class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsActiveEmployee]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class SupplyChainNodeViewSet(viewsets.ModelViewSet):
    queryset = SupplyChainNode.objects.select_related('address', 'supplier').prefetch_related('products')
    serializer_class = SupplyChainNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [SearchFilter]
    search_fields = ['address__country']

    @action(detail=False, methods=['get'])
    def by_country(self, request):
        country = request.query_params.get('country')
        if not country:
            return Response({"detail": "Параметр 'country' обязателен."}, status=400)
        nodes = self.queryset.filter(address__country__iexact=country)
        serializer = self.get_serializer(nodes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def with_high_debt(self, request):
        avg_debt = self.queryset.aggregate(avg=Avg('debt'))['avg'] or 0
        nodes = self.queryset.filter(debt__gt=avg_debt)
        serializer = self.get_serializer(nodes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_product(self, request):
        product_id = request.query_params.get('product_id')
        if not product_id:
            return Response({"detail": "Параметр 'product_id' обязателен."}, status=400)
        nodes = self.queryset.filter(products__id=product_id)
        serializer = self.get_serializer(nodes, many=True)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('node').filter(is_active=True)
    serializer_class = EmployeeSerializer
    permission_classes = [IsActiveEmployee]

