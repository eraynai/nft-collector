from django.db import models

# Create your models here.


class Nft(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
