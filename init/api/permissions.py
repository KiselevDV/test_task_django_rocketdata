from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'is_active') and request.user.is_active
