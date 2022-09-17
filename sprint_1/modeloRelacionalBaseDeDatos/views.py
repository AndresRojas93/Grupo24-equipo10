#from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from modeloRelacionalBaseDeDatos.models import Empleado, Rol, Empresas
from django.http import JsonResponse


#____________________TABLA EMPLEADOS______________________
    
class EmpleadoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


        #FUNCION PARA OBTENER EMPLEADOS      

    def get(self,request,idempleado=""):

        if len(idempleado)>0:
            empleado=list(Empleado.objects.filter(id_empleado=idempleado).values())
            if len(empleado)>0:
                datos={'Empleado': empleado}
            else:
                datos={'mensaje': 'No se encontraron empleados'}
        else:
            empleado=list(Empleado.objects.values()) 
            if len(empleado)>0:
                datos={"mensaje":empleado}
            else:
                datos={"mensaje":"No se encontraron empleados."}

        return JsonResponse(datos)


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


    
        
        

    
    


    

            
       

         



        
