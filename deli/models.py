from django.db import models

# Create your models here.
class Restaurant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=254, 
        unique=True,
    )
    phone = models.CharField(
        max_length=10,
    )
    address = models.CharField(
        max_length=500,
    )
    sunday = models.BooleanField()
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    openTime = models.TimeField()
    closeTime = models.TimeField()


class FoodItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    restaurant = models.ForeignKey(Restaurant, related_name='foodItem')
