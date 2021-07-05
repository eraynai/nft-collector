from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Nft


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


def nfts_detail(request, nft_id):
    nft = Nft.objects.get(id=nft_id)
    return render(request, 'nfts/detail.html', {'nft': nft})
