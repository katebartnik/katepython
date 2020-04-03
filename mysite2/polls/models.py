from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    picture = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=13)
    short_description = models.TextField()