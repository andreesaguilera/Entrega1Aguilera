from django.urls import path
from usuarios.views import list_users, create_user

urlpatterns = [
    #path('create_user/', create_user),
    path('list_users/', list_users) ,
    path('create_user/', create_user)
]