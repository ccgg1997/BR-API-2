from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    duenio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    fecha_ultimo_pedido = models.DateField(auto_now_add=True)
    fecha_ultima_llaamada = models.DateField(auto_now_add=True)
    fecha_creacion = models.DateField(auto_now_add=True, blank=True)
    fecha_modificacion = models.DateField(auto_now=True, blank=True)
    activo = models.BooleanField()

    def save(self, *args, **kwargs):
        self.fecha_modificacion = timezone.now()
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.barrio}"
