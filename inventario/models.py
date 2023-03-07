from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    created = models.DateTimeField(null = True)
    datecompleted = models.DateTimeField(null = True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
           return self.title

class Department(models.Model):
    nombre = models.CharField(max_length = 100)
    detalle = models.CharField(max_length = 200,blank = True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
           return self.nombre 

class TipoMercancia(models.Model):
    Tipo = models.CharField(max_length = 100)
    descripcion = models.TextField(blank = True,max_length = 100)
    creado = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
           return self.Tipo          

class Product(models.Model):
    codigo = models.CharField(max_length = 100,default='123')
    nombre = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300,blank = True)
    detalle = models.CharField(max_length = 100,null=True)
    #departamento = models.CharField(max_length=1,default=1)
    precio= models.DecimalField(decimal_places=5,max_digits=10,null=True)
    departamento= models.ForeignKey(Department, on_delete = models.CASCADE)
    tipo = models.ForeignKey(TipoMercancia, on_delete = models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    producto_imagen = models.ImageField(null=True,blank=True,default="",upload_to="images/")
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
           return self.nombre       

class gallery(models.Model):
    image = models.ImageField(upload_to="images/")   

    def __str__(self):
           return self.image.url  

class Departamento(models.Model):
    nombre = models.CharField(max_length = 100)
    detalle = models.CharField(max_length = 200,blank = True)
    descripcion = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
           return self.nombre       

class Producto(models.Model):
    codigo = models.CharField(max_length = 100,default='123')
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 300,blank = True)    
    precio= models.DecimalField(decimal_places=5,max_digits=10,default=0)
    departamento= models.ForeignKey(Departamento, on_delete = models.CASCADE)
    tipo = models.ForeignKey(TipoMercancia, on_delete = models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    producto_imagen = models.ImageField(upload_to="images/",default="")
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
           return self.nombre  


                            

