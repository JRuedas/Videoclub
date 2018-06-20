from django.db import models

class movie(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    descripcion = models.CharField(max_length=2000, null=False)
    fecha = models.DateField(null=False)
    director = models.CharField(max_length=100, null=False)
    url_portada = models.CharField(max_length=300, null=False)
    valoracion = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    url_video = models.CharField(max_length=300)
    presupuesto = models.DecimalField(max_digits=100, decimal_places=2)
    ingresos = models.DecimalField(max_digits=100, decimal_places=2)
    lenguaje = models.CharField(max_length=100)