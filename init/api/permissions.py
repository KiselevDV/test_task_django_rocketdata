from rest_framework.permissions import BasePermission

class IsActiveEmployee(BasePermission):
    def has_permission(self, request, view):
        employee = request.user.employee
        return employee.is_active if employee else False
