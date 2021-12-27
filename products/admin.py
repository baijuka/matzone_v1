from django.contrib import admin
from .models import Product, Category, ProductVariation


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductVariationAdmin(admin.TabularInline):
    model = ProductVariation
    list_display = (
        'product',
        'size',
        'price',
        'stock',
    )
    extra =1
    ordering = ("price",)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariationAdmin,]
    list_display = (
        'sku',
        'name',
        'category',
        'baseprice',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
