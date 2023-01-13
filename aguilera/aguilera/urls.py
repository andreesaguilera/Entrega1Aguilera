from .views import index, hola_mundo, vista_con_edad, vista_con_template, contex_1


"""aguilera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo),
    path('edad/<int:edad>/', vista_con_edad),
    path('template/', vista_con_template),
    path('context/', contex_1),

    path('ventas/', include('ventas.urls')),
    path('alquileres/', include('alquileres.urls')),
    path('temporales/', include('temporales.urls')),
    path('products/', include('productos.urls')),
    path('users/', include('usuarios.urls')) 
]
