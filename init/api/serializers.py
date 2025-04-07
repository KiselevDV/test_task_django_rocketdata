from rest_framework import serializers

from init.models import Address, Product, SupplyChainNode, Employee


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class SupplyChainNodeSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), source='address', write_only=True
    )
    products = ProductSerializer(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all(), write_only=True, source='products'
    )
    supplier = serializers.PrimaryKeyRelatedField(queryset=SupplyChainNode.objects.all(), allow_null=True)
    level = serializers.IntegerField(read_only=True)

    class Meta:
        model = SupplyChainNode
        fields = '__all__'
        read_only_fields = ['debt']
