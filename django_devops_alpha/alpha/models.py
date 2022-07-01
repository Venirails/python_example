from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from beta.models import Product

class Reviews(models.Model):
    rating = models.IntegerField(blank=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    review_headline = models.TextField(max_length=50, blank=False)
    review_details = models.TextField(max_length=200, blank=True)
    product= models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


