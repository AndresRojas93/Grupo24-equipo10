#from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from modeloRelacionalBaseDeDatos.models import Empleado, Rol, Empresas, Reporte_contable
from django.http import JsonResponse



#____________________TABLA EMPRESAS______________________

class EmpresasView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #FUNCION PARA OBTENER EMPRESAS

    def get(self,request,idempresas=""):  #FUNCIÓN PARA BUSCAR EMPRESA INDIVIDUALMENTE MEDIANTE EL ID

        if len(idempresas)>0:
            empresa=list(Empresas.objects.filter(id_empresas=idempresas).values())
            if len(empresa)>0:
                datos={'Empresa':empresa}
            else:
                datos={'mensaje':"No se encontró la empresa."} 
        else:
            empresa=list(Empresas.objects.values()) #Empresas es del modelo Empresas y empresa es una variable nueva 
            if len(empresa)>0:
                datos={"mensaje":empresa}
            else:
                datos={"mensaje":"No se encontraron empresas."}

        return JsonResponse(datos)

    #FUNCION PARA CREAR EMPRESAS

    def post(self,request):
        data=json.loads(request.body)
        empresa=Empresas(id_empresas=data['id_empresas'],nombre=data['nombre'],direccion=data['direccion'],ciudad=data['ciudad'],nit=data['nit'],sector_produc=data['sector_produc'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
        empresa.save()
        datos={'mensaje':'Empresa registrada exitosamente.'}

        return JsonResponse(datos)

    #FUNCION PARA ACTUALIZAR EMPRESAS

    def put(self,request,idempresas): 
        data=json.loads(request.body)
        empresa=list(Empresas.objects.filter(id_empresas=idempresas).values()) #este es el formato lista para la lectura del json
        if len(empresa)>0:
                empre=Empresas.objects.get(id_empresas=idempresas)  
                empre.nombre=data["nombre"]
                empre.direccion=data["direccion"]
                empre.ciudad=data["ciudad"]
                empre.nit=data["nit"]
                empre.sector_produc=data["sector_produc"]
                empre.telefono=data["telefono"]
                empre.fecha_creacion=data["fecha_creacion"]
                empre.save()
                mensaje = {"mensaje":"Empresa actualizada exitosamente."}
        else:
            mensaje={"mensaje":"No se encontró la empresa."}
            
        return JsonResponse(mensaje)

    #FUNCION PARA ELIMINAR EMPRESAS

    def delete(self,request,idempresas):
        empresa=list(Empresas.objects.filter(id_empresas=idempresas).values())
        if len(empresa)>0:
            Empresas.objects.filter(id_empresas=idempresas).delete()
            mensaje={"mensaje": "Empresa eliminada exitosamente."}
        else:
            mensaje={"mensaje": "No se encontró la empresa."}

        return JsonResponse(mensaje)


#______________________TABLA ROL______________________


class RolView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

        #FUNCION PARA OBTENER UN ROL
    
    def get(selft,request,Id_rol=""):

        if len(Id_rol)>0:
            rol=list(Rol.object.filter(id_rol=Id_rol).values())
            if len(rol)>0:
                datos={'Rol':rol}

            else:
                datos={'mensaje': "No se encontró el Rol."}
        
        else:
            Roles=list(Rol.objects.values())
            if len(Roles)>0:
                datos={"mensaje":Roles}
            else:
                datos={"mensaje":"No se encontro el Rol."}

        return JsonResponse(datos)

         #FUNCION PARA INGRESAR UN ROL

    def post(self,request):
        data=json.loads(request.body)
        rol=Rol(id_rol=data['id_rol'],tipo=data['tipo'])
        rol.save()
        datos={'mensaje':'Rol registrado exitosamente.'}

        return JsonResponse(datos)
    

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


         #FUNCION PARA ACTUALIZAR EMPLEADOS
         

    def put(self,request,idempleado):
        data=json.loads(request.body)
        empleado=list(Empleado.objects.filter(id_empleado=idempleado).values())
        if len(empleado)>0:
            roles=Rol.objects.get(id_rol=data["rol"])
            empre=Empresas.objects.get(id_empresas=data["empresas_id"])
            emple=Empleado.objects.update(empresas_id=empre, rol_id=roles,nombre=data['nombre'],apellido=data['apellido'],email=data['email'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
            emple.save()
            mensaje={"mensaje":"Empleado actualizado exitosamente"}

        return JsonResponse(mensaje)
            



        #_______TABLA REPORTE CONTABLE_______

class Reporte_contableView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

        #FUNCION PARA OBTENER REPORTE CONTABLE

    def get(self,request,idestado=""):

        if len(idestado)>0:
            estado=list(Reporte_contable.objects.filter(id_estado=idestado).values())
            if len(estado)>0:
                datos={'Estado':estado}
            else:
                datos={'mensaje':"No se encontró el Estado Financiero."} 
        else:
            estado=list(Reporte_contable.objects.values())
            if len(estado)>0:
                datos={"mensaje":estado}
            else:
                datos={"mensaje":"No se encontro ningun Reporte."}

        return JsonResponse(datos)



    
        
        

    
    


    

            
       

         



        
