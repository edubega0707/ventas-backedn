from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarifa(models.Model):

    Nombre      = models.CharField(max_length=100,blank=True,null=True)
    Precio1     = models.FloatField(blank=True,null=True)
    Rango1      = models.FloatField(blank=True,null=True)
    Precio2     = models.FloatField(blank=True,null=True)
    Rango2      = models.FloatField(blank=True,null=True)
    Precio3     = models.FloatField(blank=True,null=True)
    Rango3      = models.FloatField(blank=True,null=True)
    Precio4     = models.FloatField(blank=True,null=True)
    Rango4      = models.FloatField(blank=True,null=True)
    Precio5     = models.FloatField(blank=True,null=True)
    Rango5      = models.FloatField(blank=True,null=True)
    Precio6     = models.FloatField(blank=True,null=True)
    Rango6      = models.FloatField(blank=True,null=True)
    Precio7     = models.FloatField(blank=True,null=True)
    Rango7      = models.FloatField(blank=True,null=True)
    Precio8     = models.FloatField(blank=True,null=True)
    Rango8      = models.FloatField(blank=True,null=True)
    Precio9     = models.FloatField(blank=True,null=True)
    Rango9      = models.FloatField(blank=True,null=True)
    Precio10    = models.FloatField(blank=True,null=True)
    Rango10     = models.FloatField(blank=True,null=True)
    Precio11    = models.FloatField(blank=True,null=True)
    Rango11     = models.FloatField(blank=True,null=True)
    Precio12    = models.FloatField(blank=True,null=True)
    Rango12     = models.FloatField(blank=True,null=True)
    medida      = models.CharField(max_length=50)
    IdMaterial  = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

