from rest_framework import serializers
from .models import Tarifa


class Tarifaserializer(serializers.ModelSerializer):
    class Meta:
        model=Tarifa
        fields='__all__'

class CreditoTarifaserializer(serializers.ModelSerializer):
    class Meta:
        model=Tarifa
        fields=('Nombre','Precio1','Rango1','Precio2','Rango2','Precio3','Rango3','Precio4','Rango4','medida')



class AnticipadoTarifaserializer(serializers.ModelSerializer):
    class Meta:
        model=Tarifa
        fields=('Nombre','Precio9','Rango9','Precio10','Rango10','Precio11','Rango11','Precio12','Rango12','medida')