from django.urls import path, include
from init.views import supply_chain_nodes_list

app_name = 'init'

urlpatterns = [
    path('api/', include('init.api.urls')),
    path('nodes/', supply_chain_nodes_list, name='nodes-list'),
]
