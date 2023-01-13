from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import User

# Create your views here.

def list_users(request):
    users = User.objects.all()
    context = {
      'users' : users,
    }
    return render(request, 'users/list_users.html', context)

def create_user(request):
    users = User.objects.create(nombre='Andres', apellido='Aguilera', edad=33, password='andrespass', email='andres@gmail.com', telefono='+5493512663322')
    return HttpResponse('Usuario Creado')

