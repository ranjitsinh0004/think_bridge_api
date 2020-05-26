from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

Product_CHOICES = ( 
        ("1", "Beverages"), 
        ("2", "Snacks"), 
    )

class Product(models.Model):
    choice = models.CharField( 
        max_length = 20, 
        choices = Product_CHOICES, 
        default = '1'
        ) 
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    '''def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])'''