from django.shortcuts import render
from django.http import HttpResponse

from .models import Venta

def list_ventas(request):    
    all_ventas = Venta.objects.all()
    context = {
      'ventas': all_ventas
    }
    return render(request, 'ventas/list_ventas.html', context)

def create_venta(request):
    if request.method == 'GET':      
      return render(request, 'ventas/create_venta.html', context={})

    else:
      print(request.POST)
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      antiguedad = request.POST.get('antiguedad')
      credito = request.POST.get('credito')
      imagen = request.POST.get('imagen')
      Venta.objects.create(nombre = nombre, precio = precio, descripcion = descripcion, antiguedad = antiguedad, credito = credito, imagen = imagen)
      return render(request, 'ventas/create_venta.html', context={})



