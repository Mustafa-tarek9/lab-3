from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_available', 'created_at')
    search_fields = ('name', 'description')
