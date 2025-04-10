from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from init.models import APIKey, Employee


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        key = request.headers.get('Authorization')
        if not key or not key.startswith('Api-Key '):
            return None

        raw_key = key.split(' ')[1]
        try:
            api_key = APIKey.objects.get(key=raw_key)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key.')

        employee = Employee.objects.filter(node=api_key.node, is_active=True).first()
        if not employee:
            raise AuthenticationFailed('No active employee found for this node.')

        return (employee, None)
