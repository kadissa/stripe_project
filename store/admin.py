from django.contrib import admin
from .models import Item, OrderItem, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "total_price")
    inlines = [OrderItemAdmin]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("item", "order", "quantity", "items_price")


admin.site.site_header = 'Test Admin'
