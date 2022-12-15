from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from myapp.models import Product
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price_ht = models.FloatField(blank=True)
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)