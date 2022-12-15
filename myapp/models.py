from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images')
    seller_name = models.ForeignKey(User,on_delete=models.CASCADE)

# class cart(models.Model):
#     # def __str__(self):
#     #     return self.user
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     status = models.BooleanField(default=False)
#     added_on =models.DateTimeField(auto_now_add=True,null=True)

