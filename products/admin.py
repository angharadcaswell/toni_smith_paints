from django.contrib import admin
from .models import Product, Category, Size


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'image',
        'description',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)