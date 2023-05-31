from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product_sku']
    readonly_fields = ('product_sku', 'order', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'updated']
    list_filter = ['user', 'created', 'updated']
    readonly_fields = ('id', 'user', 'comment', 'created', 'updated',)
    inlines = [OrderItemInline]
