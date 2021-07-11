from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nfts/', views.nfts_index, name='index'),
    path('nfts/create', views.NftCreate.as_view(), name='nft_create'),
    path('nfts/<int:nft_id>/', views.nfts_detail, name='detail'),
    path('nfts/<int:pk>/update/',
         views.NftUpdate.as_view(), name="nft_update"),
    #     path('nfts/<int:nft_id>/delete/', views.nfts_delete),
    path('nfts/<int:pk>/delete', views.NftDelete.as_view(), name='nft_delete'),
    #     path('nfts/<int:nft_id>/edit/', views.nfts_edit),
    #     path('nfts/<int:nft_id>/submit_update_form/', views.nfts_update),
    path('nfts/<int:nft_id>/add_bid', views.add_bid, name='add_bid'),
    path('nfts/<int:nft_id>/assoc_category/<int:category_id>/',
         views.assoc_category, name='assoc_category'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/update/',
         views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/',
         views.CategoryDelete.as_view(), name='category_delete'),
]
