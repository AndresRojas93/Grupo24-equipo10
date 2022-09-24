from django.urls import path
from modeloRelacionalBaseDeDatos.views import EmpleadoView, EmpresasView, RolView, EmpleadoView, Reporte_contableView

urlpatterns = [
    path('Empresas/', EmpresasView.as_view(), name= 'Listar'),
    path('Empresas/<str:idempresas>', EmpresasView.as_view(), name= 'Buscar'), #esta ruta nos sirve para consultar, agregar, actualizar y eliminar las empresas
    path('Empleado/', EmpleadoView.as_view(), name= 'Listar'),
    path('Empleado/<str:idempleado>', EmpleadoView.as_view(), name= 'Buscar'),
    path('Rol/',RolView.as_view(), name= 'Rol'),
    path('ReporteContable/',Reporte_contableView.as_view(), name= 'Reporte_contable'),
]

