from django.db import models
from django.db.models import Min
from decimal import Decimal



class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    baseprice = models.DecimalField(max_digits=6,decimal_places=2, default=0, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def update_baseprice(self):
        self.baseprice = self.variations.aggregate(Min('price'))['price__min'] or 0
        self.save()
    
    def __str__(self):
        return self.name

   
class ProductVariation(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="variations")
    size = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=True)


    def __str__(self):
        return self.product.name +' ('+self.size+')'
