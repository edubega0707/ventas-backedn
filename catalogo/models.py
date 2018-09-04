from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    categoria=models.CharField(max_length=100)
    def __str__(self):
        return self.categoria
    def get_absolute_url(self):
        return reverse('index:catalogogeneral')

class Producto(models.Model):
    titulo=models.CharField(max_length=100)
    categorias = models.ForeignKey(Categoria, related_name='categorias', on_delete=models.CASCADE)
    descargable=models.FileField(upload_to='exp/', null=True, blank=True)
    descripcion=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.titulo
    def get_absolute_url(self):
        return reverse('index:detalle', kwargs={'pk': self.pk})