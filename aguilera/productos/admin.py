from django.contrib import admin
from productos.models import Producto

#admin.site.register(Producto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'stock')
    list_filter = ('nombre', 'precio', 'descripcion', 'stock') #Filtro lateral
    search_fields = ('nombre', 'precio', 'descripcion', 'stock') #Buscador
    



