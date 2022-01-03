from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Product, ProductVariation, Review


@receiver(post_save, sender=ProductVariation)
def update_baseprice(sender, instance, created, **kwargs):
    
    instance.product.update_baseprice()


@receiver(post_delete, sender=ProductVariation)
def update_baseprice(sender, instance, **kwargs):
    instance.product.update_baseprice()

@receiver(post_save, sender=Review)
def update_rating(sender, instance, created, **kwargs):
    
    instance.product.update_rating()