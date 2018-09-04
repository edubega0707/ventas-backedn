from import_export import  resources
#from import_export.fields import Field
from .models import Tarifa



class TarifaResource(resources.ModelResource):
    class Meta:
        model = Tarifa
        import_id_fields = ('Nombre',)
        fields= ('Nombre', 'Precio1', 'Rango1', 'Precio2', 'Rango2', 'Precio3', 'Rango3', 'Precio4', 'Rango4', 'Precio5', 'Rango5', 'Precio6', 'Rango6', 'Precio7', 'Rango7', 'Precio8', 'Rango8', 'Precio9', 'Rango9', 'Precio10', 'Rango10', 'Precio11', 'Rango11', 'Precio12', 'Rango12', 'medida','IdMaterial',)

