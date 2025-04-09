from rest_framework.permissions import BasePermission

class IsActiveEmployee(BasePermission):
    def has_permission(self, request, view):
        try:
            return request.user.employee.is_active
        except AttributeError:
            return False
