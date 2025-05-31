# my_zhengze/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    is_on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)