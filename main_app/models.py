from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name} is {self.description}'

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Nft(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs=('nft_id', self.id))


class Bids(models.Model):
    date = models.DateField()
    bid = models.FloatField()
    user = models.CharField(max_length=250)
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bid} on {self.nft} by {self.user} on {self.date}'


class Photos(models.Model):
    url = models.CharField(max_length=250)
    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for nft_id: {self.nft_id} @{self.url}"
