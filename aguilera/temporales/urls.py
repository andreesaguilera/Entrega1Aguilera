from django.urls import path
from .views import create_temporal, list_temporales

urlpatterns = [
    path('create-temporal/', create_temporal),
    path('list-temporales/', list_temporales) 
]