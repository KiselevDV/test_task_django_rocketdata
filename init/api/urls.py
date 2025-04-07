from rest_framework.routers import DefaultRouter

from init.api.views import AddressViewSet, ProductViewSet, SupplyChainNodeViewSet, EmployeeViewSet


router = DefaultRouter()
router.register('addresses', AddressViewSet)
router.register('products', ProductViewSet)
router.register('nodes', SupplyChainNodeViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = router.urls
