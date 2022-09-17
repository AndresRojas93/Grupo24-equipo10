import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from modeloRelacionalBaseDeDatos.models import Empresas
from django.http import JsonResponse

from sprint_2.modeloRelacionalBaseDeDatos.models import Empleado
#from django.shortcuts import render

# Create your views here.

class EmpresasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id_empresas=""):

        if len(id_empresas)>0:
            empresa=list(Empresas.object.filter(Id_empresas=id_empresas).values())
            if len(empresa)>0:
                datos={'Empresa':empresa}

            else:
                datos={'mensaje': "No se encontro la Empresa."}
        
        else:
            empresas=list(Empresas.objects.values())
            if len(empresas)>0:
                datos={"mensaje":Empresas}
            else:
                datos={"mensaje":"No se encontraron Empresas."}

        return JsonResponse(datos)


    def post(self,request):
            data=json.loads(request.body)
            empresa=Empresas(id_empresas=data['id_empresas'],nombre=data['nombre'],ciudad=data['ciudad'],nit=data['nit'],sector_produc=data['sector_produc'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
            empresa.save()
            datos={'mensaje': 'Empresa Registrada Exitosamente'}
            return JsonResponse(datos)
        
    def put(self,request,id_empresas):
            data=json.loads(request.body)
            empresa=list(Empresas.objects.filter(Id_empresas=id_empresas).values())
            if len (empresa>0):
                emp=Empresas.objects.get(Id_empresas=id_empresas)
                emp.nombre=data["nombre"]
                emp.direccion=data["direccion"]
                emp.ciudad =data["ciudad"]
                emp.nit = data["nit"]
                emp.sector_produc= data["sector_produc"]
                emp.telefono = data["telefono"]
                emp.fecha_creacion =data["fecha_creacion"]
                emp.save()
                mensaje = {"mensaje":"Empresa actualizada exitosamente"}
            else:
                mensaje={"mensaje":"No se encontro la empresa"}
            
            return JsonResponse(mensaje)
        

          #FUNCION PARA AGREGAR EMPLEADOS

    def post (self,request):
        data=json.loads(request.body)
        print(data)
        roles=Rol.objects.get(id_rol=data["rol"])
        empre=Empresas.objects.get(id_empresas=data["empresas_id"])
        emple=Empleado.objects.create(id_empleado=data["id_empleado"],empresas_id=empre, rol=roles,nombre=data['nombre'],apellido=data['apellido'],email=data['email'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
        emple.save()
        mensaje={"Mensaje":"Empleado registrado exitosamente"}

        return JsonResponse(mensaje)
    
        
    def put(self,request,id_empleado):
            data=json.loads(request.body)
            empleado=list(Empleado.objects.filter(Id_empleado=id_empleado).values())
            if len (empleado)>0:
                emp=Empleado.objects.get(Id_empleado=id_empleado)
                emp.nombre=data["nombre"]
                emp.apellido=data["apellido"]
                emp.email =data["email"]
                emp.telefono = data["telefono"]
                emp.empresas_id = data["empresas_id"]
                emp.fecha_creacion =data["fecha_creacion"]
                emp.save()
                mensaje = {"mensaje":"Empleado actualizado exitosamente"}
            else:
                mensaje={"mensaje":"No se encontro el Empleado"}
            
            return JsonResponse(mensaje)
