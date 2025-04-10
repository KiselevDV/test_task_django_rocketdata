from django.urls import path, include
from rest_framework.routers import DefaultRouter

from init.api.views import (
    AddressViewSet, ProductViewSet, SupplyChainNodeViewSet, EmployeeViewSet, QRCodeEmailAPIView)


router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'nodes', SupplyChainNodeViewSet, basename='supplychainnode')
router.register(r'employees', EmployeeViewSet, basename='employee')

app_name = 'api'

urlpatterns = [
    path('send-qr/', QRCodeEmailAPIView.as_view(), name='send-qr-email'),
    path('', include(router.urls)),
]
