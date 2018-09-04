from django.contrib import admin
from .models import Producto,Categoria

from import_export.admin import ImportExportModelAdmin
from .resources import CategoriaResource, ProductoResource


class CategoriaAdmin(ImportExportModelAdmin):
    resource_class = CategoriaResource


class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource




# Register your models here.

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)