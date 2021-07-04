from django.shortcuts import render
from django.http import HttpResponse


class Nft:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


nfts = [
    Nft('Blue Window', 'A 3D model of a blue window', 1.0),
    Nft('Green Window', 'A 3D model of a green window', 1.0)
]
# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello</h1>')


def about(request):
    return render(request, 'about.html')


def home(request):
    return HttpResponse('test')


def index(request):
    return render(request, 'nfts/index.html', {'nfts': nfts})
