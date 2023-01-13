from django.urls import path
from .views import create_venta, list_ventas

urlpatterns = [
    path('create-venta/', create_venta),
    path('list-ventas/', list_ventas) 
]