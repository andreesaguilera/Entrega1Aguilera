from django.shortcuts import render
from django.http import HttpResponse

from .models import Alquiler

def list_alquileres(request):
    """ if search """
    if 'search' in request.GET:      
      all_alquileres = Alquiler.objects.filter(nombre__icontains = request.GET.get('search'))
    else:
      all_alquileres = Alquiler.objects.all()    
    
    context = {
      'alquileres': all_alquileres
    }
    return render(request, 'alquileres/list_alquileres.html', context)

def create_alquiler(request):
    if request.method == 'GET':      
      return render(request, 'alquileres/create_alquiler.html', context={})

    else:
      print(request.POST)
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      ambientes = request.POST.get('ambientes')
      expensas = request.POST.get('expensas')
      imagen = request.POST.get('imagen')
      Alquiler.objects.create(nombre = nombre, precio = precio, descripcion = descripcion, ambientes = ambientes, expensas = expensas, imagen = imagen)
      return render(request, 'alquileres/create_alquiler.html', context={})