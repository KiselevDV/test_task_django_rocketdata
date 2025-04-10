from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if hasattr(user, 'is_superuser') and user.is_superuser:
            return True
        return hasattr(user, 'is_active') and user.is_active
