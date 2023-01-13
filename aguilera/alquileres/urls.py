from django.urls import path
from .views import create_alquiler, list_alquileres

urlpatterns = [
    path('create-alquiler/', create_alquiler),
    path('list-alquileres/', list_alquileres) 
]