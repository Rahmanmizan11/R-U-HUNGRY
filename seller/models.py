from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.FileField(upload_to='profile/', null=True, blank=True)
    type = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Menu(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    retaurant = models.ForeignKey(Restaurant, on_delete=CASCADE)
    is_available = models.BooleanField(default=True)