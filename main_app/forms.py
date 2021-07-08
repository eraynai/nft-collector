from django.forms import ModelForm
from .models import Bids


class BiddingForm(ModelForm):
    class Meta:
        model = Bids
        fields = ['date', 'bid', 'user']
