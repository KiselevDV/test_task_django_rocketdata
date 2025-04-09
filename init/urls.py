from django.urls import path, include


urlpatterns = [
    path('api/', include('init.api.urls')),
]
