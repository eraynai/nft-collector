from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, Http404
from main_app.models import Nft
from django.template.loader import render_to_string


def index(request):
    return HttpResponse('<h1>Hello</h1>')


def home(request):
    return render(request, 'about.html')


def nfts_index(request):
    nfts = Nft.objects.all()
    print(nfts)
    return render(request, 'nfts/index.html', {'nfts': nfts})


def nfts_detail(request, nft_id):
    try:
        nft = Nft.objects.get(id=nft_id)
        return render(request, 'nfts/detail.html', {'nft': nft})
    except:
        data_response = render_to_string('404.html')
        return HttpResponseNotFound(data_response)


def nfts_new(request):
    return render(request, 'nfts/new_form.html')
