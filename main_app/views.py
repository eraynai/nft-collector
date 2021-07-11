from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Nft, Bids, Photos, Category
from .forms import BiddingForm
S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'nftcollec'


def home(request):
    # n = Nft.objects.get(id=19)
    # b = Bids.objects.get(id=8)
    # cool_cat = n.bids_set.remove(b)
    # print(cool_cat)
    # n = Nft.objects.all()
    # print(n)
    return render(request, 'about.html')


def nfts_index(request):
    nfts = Nft.objects.all()
    return render(request, 'nfts/index.html', {'nfts': nfts})


def nfts_detail(request, nft_id):
    try:
        # get the cat
        nft = Nft.objects.get(id=nft_id)
        # bids = nft.bids_set.all()
        # print('this is bids', bids)
        categories_nft_doesnt_have = Category.objects.exclude(
            id__in=nft.categories.all().values_list('id'))
        bidding_form = BiddingForm()
        print(bidding_form)
        return render(request, 'nfts/detail.html', {'nft': nft, 'bidding_form': bidding_form, 'categories': categories_nft_doesnt_have})
    except:
        data_response = render_to_string('404.html')
        return HttpResponseNotFound(data_response)


# def nfts_delete(request, nft_id):
#     nft = Nft.objects.get(id=nft_id)
#     nft.delete()
#     return redirect('/nfts')


# def nfts_edit(request, nft_id):
#     nft = Nft.objects.get(id=nft_id)
#     return render(request, 'nfts/edit.html', {'nft': nft})


# def nfts_update(request, nft_id):
#     nft = Nft.objects.get(id=nft_id)
#     nft.name = request.POST['name']
#     nft.description = request.POST['description']
#     nft.price = request.POST['price']
#     nft.save()
#     return redirect(f'/nfts/{nft.id}')


def add_bid(request, nft_id):
    form = BiddingForm(request.POST)
    if form.is_valid():
        new_bid = form.save(commit=False)
        new_bid.nft_id = nft_id
        new_bid.save()
    return redirect('detail', nft_id=nft_id)


class NftCreate(CreateView):
    model = Nft
    fields = ['name', 'description', 'price', 'category']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NftUpdate(UpdateView):
    model = Nft
    fields = ['name', 'description', 'price', 'category']


class NftDelete(DeleteView):
    model = Nft
    success_url = '/nfts/'


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'


class CategoryDetail(DetailView):
    model = Category


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'description']


class CategoryDelete(DeleteView):
    model = Category
    success_url = '/nfts/'


def assoc_category(request, nft_id, category_id):
    nft = Nft.objects.get(id=nft_id).categories.add(category_id)
    print(nft)
    return redirect('detail', nft_id=nft_id)
