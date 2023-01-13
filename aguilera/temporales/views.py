from django.shortcuts import render
from django.http import HttpResponse

from .models import Temporal

def list_temporales(request):    
    all_temporales = Temporal.objects.all()
    context = {
      'temporales': all_temporales
    }
    return render(request, 'temporales/list_temporales.html', context)


def create_temporal(request):
    if request.method == 'GET':      
      return render(request, 'temporales/create_temporal.html', context={})

    else:
      print(request.POST)
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      ambientes = request.POST.get('ambientes')
      temporada = request.POST.get('temporada')
      imagen = request.POST.get('imagen')
      Temporal.objects.create(nombre = nombre, precio = precio, descripcion = descripcion, ambientes = ambientes, temporada = temporada, imagen = imagen)
      return render(request, 'temporales/create_temporal.html', context={})
