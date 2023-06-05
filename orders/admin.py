from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('pack',)
    readonly_fields = ('pack', 'order', 'quantity')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'updated')
    list_filter = ('user', 'created', 'updated')
    readonly_fields = ('id', 'user', 'comment', 'created', 'updated',)
    inlines = (OrderItemInline,)
