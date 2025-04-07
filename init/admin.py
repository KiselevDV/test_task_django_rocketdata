from django.contrib import admin

from init.models import SupplyChainNode, Product, Address, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


@admin.register(SupplyChainNode)
class SupplyChainNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'supplier', 'debt', 'level', 'created_at')
    list_filter = ('supplier', 'address__city')
    search_fields = ('name', 'email')
    inlines = [EmployeeInline]
    filter_horizontal = ('products',)
    readonly_fields = ('level',)
    actions = ['clear_debt']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(modeladmin, request, queryset):
        queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')
    list_filter = ('release_date',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number')
    search_fields = ('country', 'city', 'street')
    list_filter = ('country', 'city')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'phone', 'node')
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('node',)