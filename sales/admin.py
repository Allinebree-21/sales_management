# Register your models here.
from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'price','cost_price','total_amount','profit','date')
    search_fields = ('item_name',)
    list_filter = ('date',)

