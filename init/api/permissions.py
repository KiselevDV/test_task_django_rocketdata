from rest_framework.permissions import BasePermission

from init.models import APIKey


class IsActiveEmployee(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.employee.is_active
        except AttributeError:
            return False


class HasAPIKey(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return False
        try:
            key_obj = APIKey.objects.select_related('node').get(key=api_key)
            request.supply_chain_node = key_obj.node
            return True
        except APIKey.DoesNotExist:
            return False
