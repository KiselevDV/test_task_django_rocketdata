from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from init.models import APIKey


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        key = request.headers.get('Authorization')
        if not key or not key.startswith('Api-Key '):
            return None

        raw_key = key.split(' ')[1]
        try:
            api_key = APIKey.objects.select_related('employee').get(key=raw_key)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key.')

        if not api_key.employee.is_active:
            raise AuthenticationFailed('Employee is not active.')

        return (api_key.employee, None)
