from django.contrib import admin
from .models import Transaction, Client, Sale

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'amount', 'created_at')
    search_fields = ('client_name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'price', 'date')
    list_filter = ('date', 'product_name')
    search_fields = ('product_name',)
    ordering = ('-date',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('nome', 'email')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
