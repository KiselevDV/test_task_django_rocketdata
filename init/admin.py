from django.contrib import admin

from init.models import SupplyChainNode, Product, Address, Employee, APIKey
from init.tasks import clear_debt_task


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


@admin.register(SupplyChainNode)
class SupplyChainNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'supplier_link', 'debt', 'get_level_display', 'created_at')
    list_filter = ('supplier', 'address__city')
    search_fields = ('name', 'email')
    inlines = [EmployeeInline]
    filter_horizontal = ('products',)
    readonly_fields = ('get_level_display',)
    actions = ['clear_debt']

    @admin.display(description='Поставщик')
    def supplier_link(self, obj):
        if obj.supplier:
            return f'{obj.supplier.name} (уровень {obj.supplier.level})'
        return '—'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(modeladmin, request, queryset):
        count = queryset.count()
        if count > 20:
            ids = list(queryset.values_list('id', flat=True))
            clear_debt_task.delay(ids)
            modeladmin.message_user(request, f'Очистка {count} звеньев запущена через Celery.')
        else:
            updated = queryset.update(debt=0)
            modeladmin.message_user(request, f'Очищено задолженности у {updated} звеньев.')


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
    list_display = ('last_name', 'first_name', 'email', 'phone', 'is_active', 'node')
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('node', 'is_active')


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'created_at', 'node')
