from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Nft


# class Nft:
#     def __init__(self, name, description, price):
#         self.name = name
#         self.description = description
#         self.price = price


# nfts = [
#     Nft('blue Window', 'A 3D model of a blue window', 1.0),
#     Nft('green Window', 'A 3D model of a green window', 1.0)
# ]
# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello</h1>')


def about(request):
    return render(request, 'about.html')


def home(request):
    return HttpResponse('test')


def nfts_index(request):
    nfts = Nft.objects.all()
    print(nfts)
    return render(request, 'nfts/index.html', {'nfts': nfts})
