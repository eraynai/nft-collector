from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nfts/', views.nfts_index, name='index'),
    path('nfts/<int:nft_id>/', views.nfts_detail, name='detail'),
    path('nfts/new/', views.nfts_new, name='new'),
    path('nfts/<int:nft_id>/delete/', views.nfts_delete),
]
