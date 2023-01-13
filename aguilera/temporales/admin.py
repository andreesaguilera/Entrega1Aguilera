from django.contrib import admin
from temporales.models import Temporal

@admin.register(Temporal)
class TemporalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'ambientes', 'temporada', 'imagen')
    list_filter = ('nombre', 'precio', 'descripcion', 'ambientes', 'temporada', 'imagen')
    search_fields = ('nombre', 'precio', 'descripcion', 'ambientes', 'temporada', 'imagen')
    ordering = ('nombre', 'precio', 'descripcion', 'ambientes', 'temporada', 'imagen')
    
