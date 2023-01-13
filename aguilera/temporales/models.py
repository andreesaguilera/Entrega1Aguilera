from django.db import models

class Temporal(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    ambientes = models.IntegerField()
    temporada = models.TextField()    
    imagen = models.CharField(max_length=200)    

    def __str__(self):
        return self.nombre