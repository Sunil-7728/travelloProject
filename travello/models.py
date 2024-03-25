from django.db import models

# Create your models here.
class Destinations(models.Model):

    name = models.CharField(max_length=100)

    desc = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pics')
    offer =models.BooleanField(default=False)