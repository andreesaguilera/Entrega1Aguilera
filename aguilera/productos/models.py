from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    """ imagen = models.ImageField(upload_to='productos') """
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
