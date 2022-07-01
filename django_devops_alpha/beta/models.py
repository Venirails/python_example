from django.db import models


class Brand(models.Model):
    name = models.TextField(max_length=20, blank=False)
    desc = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.TextField(max_length=20, blank=False)
    desc = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)