from django.contrib import admin
from . models import Bids, Nft

# Register your models here.
admin.site.register(Nft)
admin.site.register(Bids)
