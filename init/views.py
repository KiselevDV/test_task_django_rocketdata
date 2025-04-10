from django.shortcuts import render

from init.models import SupplyChainNode


def supply_chain_nodes_list(request):
    nodes = SupplyChainNode.objects.all()
    return render(request, 'init/nodes_list.html', {'nodes': nodes})
