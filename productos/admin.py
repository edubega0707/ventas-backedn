from django.contrib import admin
from .models import Tarifa

from import_export.admin import ImportExportModelAdmin
from .resources import  TarifaResource



class TarifaAdmin(ImportExportModelAdmin):
    resource_class = TarifaResource
    list_display = ('Nombre',  'IdMaterial')

admin.site.register(Tarifa, TarifaAdmin)