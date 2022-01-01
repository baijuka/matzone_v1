from django.contrib import admin
from .models import Product, Category, ProductVariation, Review
from .forms import ProductForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductVariationAdmin(admin.TabularInline):
    model = ProductVariation
    fields = (
        'product',
        'size',
        'price',
        'stock',
    )
    extra =1
    ordering = ("price",)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariationAdmin,]
    form = ProductForm
    list_display = (
        'sku',
        'name',
        'category',
        'baseprice',
        'rating',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review)
