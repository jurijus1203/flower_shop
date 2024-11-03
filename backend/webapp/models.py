from django.db import models

# Create your models here.

PRODUCT_TYPES = [
    ('flowers', 'Flowers'),
    
]


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    product_avaliblity = models.BooleanField(default=True)
    product_avalible_quantity = models.IntegerField(default=1)
    product_price = models.IntegerField(default=1)
    product_description = models.TextField()
    product_image = models.ImageField(null=True, blank=True, upload_to='images/')
    product_type = models.CharField(max_length=64, choices=PRODUCT_TYPES, default='flowers')

    def __str__(self) -> str:
        return f'{self.product_type} - {self.product_name}: {self.product_price}eur. Remaining qty: {self.product_avalible_quantity}pcs.'
    
    