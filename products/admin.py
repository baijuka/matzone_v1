from django.contrib import admin
from .models import Product, Category, ProductVariation

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'baseprice',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ProductVariationAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'size',
        'price',
        'stock',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
