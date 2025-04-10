from django.db.models import Avg
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

from init.models import Address, Product, SupplyChainNode, Employee
from init.tasks import send_qr_code_email
from init.api.serializers import (
    AddressSerializer, ProductSerializer, SupplyChainNodeSerializer, EmployeeSerializer, QRCodeRequestSerializer)
from init.api.permissions import IsActiveEmployee


class SupplyChainNodeViewSet(viewsets.ModelViewSet):
    queryset = SupplyChainNode.objects.select_related('address', 'supplier').prefetch_related('products')
    serializer_class = SupplyChainNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [SearchFilter]
    search_fields = ['address__country']

    def get_queryset(self):
        employee = self.request.user
        return SupplyChainNode.objects.filter(id=employee.node_id)

    @action(detail=False, methods=['get'])
    def by_country(self, request):
        country = request.query_params.get('country')
        if not country:
            return Response({'detail': 'Параметр "country" обязателен'}, status=400)
        nodes = self.get_queryset().filter(address__country__iexact=country)
        serializer = self.get_serializer(nodes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def with_high_debt(self, request):
        avg_debt = self.get_queryset().aggregate(avg=Avg('debt'))['avg'] or 0
        nodes = self.get_queryset().filter(debt__gt=avg_debt)
        serializer = self.get_serializer(nodes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_product(self, request):
        product_id = request.query_params.get('product_id')
        if not product_id:
            return Response({'detail': 'Параметр "product_id" обязателен'}, status=400)
        nodes = self.get_queryset().filter(products__id=product_id)
        serializer = self.get_serializer(nodes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='send-qr')
    def send_qr(self, request, pk=None):
        node = self.get_object()
        user_email = request.user.email
        send_qr_code_email.delay(node.id, user_email)
        return Response({'detail': f'QR код отправлен на {user_email} (Celery)'})


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsActiveEmployee]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('node').filter(is_active=True)
    serializer_class = EmployeeSerializer
    permission_classes = [IsActiveEmployee]


class QRCodeEmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = QRCodeRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        node_id = serializer.validated_data['node_id']
        email = serializer.validated_data['email']
        send_qr_code_email.delay(node_id, email)
        return Response({
            'message': 'Задача  на отправку QR кода на почту (Celery)'},
            status=status.HTTP_202_ACCEPTED
        )
