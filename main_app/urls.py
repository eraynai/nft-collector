from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nfts/', views.nfts_index, name='index'),
    path('nfts/<int:nft_id>/', views.nfts_detail, name='detail'),
    path('nfts/new/', views.nfts_new, name='new'),
    path('nfts/<int:nft_id>/delete/', views.nfts_delete),
    path('nfts/<int:nft_id>/edit/', views.nfts_edit),
    path('nfts/<int:nft_id>/submit_update_form/', views.nfts_update),
    path('nfts/<int:nft_id>/add_bid', views.add_bid, name='add_bid'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('nfts/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('nfts/<int:pk>/update/',
         views.CategoryUpdate.as_view(), name='category_update'),
    path('ntfs/<int:pk>/delete/',
         views.CategoryDelete.as_view(), name='category_delete')
]
