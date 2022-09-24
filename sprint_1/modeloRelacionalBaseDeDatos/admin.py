from django.contrib import admin

# Register your models here.
from modeloRelacionalBaseDeDatos.models import Empresas, Reporte_contable,Empleado,Rol

admin.site.register(Empresas)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(Reporte_contable)
