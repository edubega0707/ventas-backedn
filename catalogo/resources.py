from import_export import  resources
#from import_export.fields import Field
from .models import Categoria, Producto
class CategoriaResource(resources.ModelResource):
    class Meta:
        model=Categoria


class ProductoResource(resources.ModelResource):
    class Meta:
        model=Producto


