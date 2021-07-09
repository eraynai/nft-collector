from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
import uuid
import boto3
from .models import Nft, Bids, Photos
from .forms import BiddingForm
S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'nftcollec'


def home(request):
    # n = Nft.objects.get(id=13)
    # cool_cat = n.bids_set.all()
    # print(cool_cat)
    return render(request, 'about.html')


def nfts_index(request):
    if(request.method == 'POST'):
        nft = Nft.objects.create(
            name=request.POST['name'], description=request.POST['description'], price=request.POST['price'], category=request.POST['category'])
        return redirect(f'/nfts/{nft.id}')
    else:
        nfts = Nft.objects.all()
        print(nfts)
        return render(request, 'nfts/index.html', {'nfts': nfts})


def nfts_detail(request, nft_id):
    try:
        # get the cat
        nft = Nft.objects.get(id=nft_id)
        # bids = nft.bids_set.all()
        # print('this is bids', bids)
        bidding_form = BiddingForm()
        print(bidding_form)
        return render(request, 'nfts/detail.html', {'nft': nft, 'bidding_form': bidding_form})
    except:
        data_response = render_to_string('404.html')
        return HttpResponseNotFound(data_response)


def nfts_new(request):
    return render(request, 'nfts/new_form.html')


def nfts_delete(request, nft_id):
    nft = Nft.objects.get(id=nft_id)
    nft.delete()
    return redirect('/nfts')


def nfts_edit(request, nft_id):
    nft = Nft.objects.get(id=nft_id)
    return render(request, 'nfts/edit.html', {'nft': nft})


def nfts_update(request, nft_id):
    nft = Nft.objects.get(id=nft_id)
    nft.name = request.POST['name']
    nft.description = request.POST['description']
    nft.price = request.POST['price']
    nft.save()
    return redirect(f'/nfts/{nft.id}')


# def add_bid(request, nft_id):
#     form = BiddingForm(request.POST)
#     if form.is_valid():
#         new_bid = form.save(commit=False)
#         new_bid.nft_id = nft_id
#         new_bid.save()
#     return redirect('detail', nft_id=nft_id)
