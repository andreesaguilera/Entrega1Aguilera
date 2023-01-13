from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto
from .forms import ProductoForm


def create_product(request):
    if request.method == 'GET':
      context = {
        'form': ProductoForm()
      }
      return render(request, 'products/create_product.html', context=context)

    else:
      print(request.POST)
      nombre = request.POST.get('nombre')
      precio = request.POST.get('precio')
      descripcion = request.POST.get('descripcion')
      stock = request.POST.get('stock')
      Producto.objects.create(nombre = nombre, precio = precio, descripcion = descripcion, stock = stock)
      return render(request, 'products/create_product.html', context={})
      



    """ #Producto.objects.create(nombre = "Mouse Genius", precio = 2500, descripcion = 'Mouse Genius Inalambrico', stock = 20)
    Producto.objects.create(nombre = "Teclado Genius", precio = 4300, descripcion = 'Teclado Genius Inalambrico', stock = 15)
    return HttpResponse("Se Creo el Nuevo Producto") """

def list_prodcuts(request):
    # filtrar productos
    if 'search' in request.GET:
      search = request.GET.get('search')
      all_products = Producto.objects.filter(nombre__icontains = search)
    else:
      all_products = Producto.objects.all()
    context = {
      'products': all_products
    }
    return render(request, 'products/list_products.html', context)

""" def list_prodcuts(request):    
    all_products = Producto.objects.all()
    context = {
      'products': all_products
    }
    return render(request, 'products/list_products.html', context) """


    