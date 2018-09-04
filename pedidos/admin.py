from django.contrib import admin
from .models import Cliente,Orden,Pedido, DomCliente, Archivo,Archivodos

from import_export.admin import ImportExportModelAdmin
from .resources import ClienteResource, OrdenResource, DomClienteResource, PedidoResource, ArchivoResource,ArchivodosResource



class ClienteAdmin(ImportExportModelAdmin):
    resource_class = ClienteResource
    list_display = ('NOMBRE','CORREO')


class OrdenAdmin(ImportExportModelAdmin):
    resource_class = OrdenResource

class DomclienteAdmin(ImportExportModelAdmin):
    resource_class = DomClienteResource


class PedidoAdmin(ImportExportModelAdmin):
    resource_class = PedidoResource




class ArchivoAdmin(ImportExportModelAdmin):
    resource_class = ArchivoResource

class ArchivodosAdmin(ImportExportModelAdmin):
    resource_class = ArchivodosResource




admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DomCliente, DomclienteAdmin)
admin.site.register(Archivo, ArchivoAdmin)
admin.site.register(Archivodos, ArchivodosAdmin)