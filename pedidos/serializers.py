from rest_framework import serializers
from .models import Cliente,Orden,Pedido, DomCliente, Archivo, Archivodos
from productos.models import Tarifa

from django.contrib.auth.models import User


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'

    def create(self, validated_data):
        cliente=Cliente.objects.create(**validated_data)
        cliente.save()
        return cliente

class CodigoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('CODIGO')

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Archivo
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        archivo = Archivo.objects.create(**validated_data)
        archivo.save()


        return archivo

class ArchivodosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Archivodos
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        archivo = Archivodos.objects.create(**validated_data)
        archivo.save()
        return archivo


class ProductoTarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarifa
        fields='__all__'


class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model=DomCliente
        fields='__all__'

    def create(self, validated_data):
        print(validated_data)
        domicilio = DomCliente.objects.create(**validated_data)
        domicilio.save()

        return domicilio


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username',]



class PedidoArticulosSerializer(serializers.ModelSerializer):
    producto=ProductoTarifaSerializer(many=False, read_only=True)
    producto_id=(serializers.PrimaryKeyRelatedField(
        queryset=Tarifa.objects.all(),
        write_only=True,
        required=False,
        many=False))

    class Meta:
        model=Pedido
        fields='__all__'


class OrdenSerializer(serializers.ModelSerializer):
    cliente_dom = DomicilioSerializer(many=True, read_only=True)
    items=PedidoArticulosSerializer(many=True )
    fechageneracion = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model=Orden
        fields='__all__'

    def create(self,validated_data):
        print(validated_data)
        datos_orden=validated_data.pop('items')
        orden=Orden.objects.create(**validated_data)

        for o in datos_orden:
            print(o)
            pro_id   =o['producto_id']
            cantidad =o['cantidad']
            subtotal =o['subtotal']
            Pedido.objects.create(orden=orden, cantidad=cantidad, subtotal=subtotal,  producto=pro_id)

        return orden


class OrdenClienteSerializer(serializers.ModelSerializer):
    #domicilio_extra = DomicilioSerializer(many=False, read_only=True)
    items = PedidoArticulosSerializer(many=True)
    cliente=ClienteSerializer(many=False, read_only=True)
    fechageneracion = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)


    class Meta:
        model=Orden
        fields= '__all__'



class ContadoTarifaserializer(serializers.ModelSerializer):
    class Meta:
        model=Tarifa
        fields=('Nombre','Precio5','Rango5','Precio6','Rango6','Precio7','Rango7','Precio8','Rango8','medida')