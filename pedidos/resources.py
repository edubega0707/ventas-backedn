from import_export import  resources

from import_export.fields import Field
from .models import Cliente, DomCliente, Orden, Pedido, Archivo,Archivodos
from productos.models import  Tarifa
class ClienteResource(resources.ModelResource):
    class Meta:
        model=Cliente
        import_id_fields=('CODIGO',)
        fields=('CODIGO','NOMBRE','DIRECCIÓN','COLONIA','POBLACIÓN','MUNICIPIO','CP','RFC','TELÉFONO','CORREO',)


class DomClienteResource(resources.ModelResource):
    class Meta:
        model=DomCliente


class OrdenResource(resources.ModelResource):
    #full_dom=Field()
    class Meta:
        model=Orden
        widgets = {
            'fechageneracion': {'format': '%d-%m-%Y'},
        }

        #def dehydrate_full_dom(self, orden):
        #    return '%s , %s , %s, %s' % (orden.domicilio_extra.calle, orden.domicilio_extra.colonia, orden.domicilio_extra.poblacion, orden.domicilio_extra.poblacion.cp)


class PedidoResource(resources.ModelResource):
    class Meta:
        model=Pedido
        fields = ('orden__numerodeorden', 'producto__Nombre', 'cantidad', 'subtotal')


class ArchivoResource(resources.ModelResource):
    class Meta:
        model=Archivo

class ArchivodosResource(resources.ModelResource):
    class Meta:
        model=Archivodos