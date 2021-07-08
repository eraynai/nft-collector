from django.db import models

# Create your models here.


class Nft(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Bids(models.Model):
    date = models.DateField()
    bid = models.FloatField()
    user = models.CharField(max_length=250)
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bid} by {self.user} on {self.date}'
