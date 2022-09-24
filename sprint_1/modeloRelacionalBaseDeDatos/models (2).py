from ast import Delete
import email
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo

class Administrador(models.Model):
    id_usuario= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Empresas(models.Model):
    id_empresas = models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=45)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=45)
    nit = models.CharField(max_length=45)
    sector_produc = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    id_empleado= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=45)
    empresas_id = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre+" "+ self.apellido

class Reporte_contable(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=45)
    fecha = models.DateTimeField(auto_now=True)
    empleado_id = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    empleado_empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    empleado_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    monto = models.IntegerField 


class Usuario_app (models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    usuario = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    contraseña = models.CharField(max_length=45)
    empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)

class Comprobantes (models.Model):
    contabilidad = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True)
    valor = models.IntegerField
    empresas_id = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte_contable, on_delete=models.CASCADE)










