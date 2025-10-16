from django.contrib import admin

from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'amount', 'created_at')
    search_fields = ('client_name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
