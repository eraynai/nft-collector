from django.contrib import admin
from . models import Bids, Nft, Photos

# Register your models here.
admin.site.register(Nft)
admin.site.register(Bids)
admin.site.register(Photos)
