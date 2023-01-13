from django.urls import path
from productos.views import create_product, list_prodcuts

urlpatterns = [
    path('create-product/', create_product),
    path('list-products/', list_prodcuts) 
]