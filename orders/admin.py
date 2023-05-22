from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product_sku']
    readonly_fields = ('product_sku', 'order', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'email', 'city', 'created', 'updated']
    list_filter = ['company', 'created', 'updated']
    readonly_fields = ('id', 'uuid', 'company', 'name', 'email', 'phone',
                       'city', 'comment', 'created', 'updated',)
    inlines = [OrderItemInline]
