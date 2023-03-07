from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm, ProductForm
from .models import Task, Department,Product,gallery,TipoMercancia
from .models import Departamento,Producto
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):   
    return render(request,'home.html')
def menu(request):   
    return render(request,'menulateral.html')    
def galeria(request):   
    object_list = Producto.objects.all()
    deptos = Departamento.objects.all()
    tipo = TipoMercancia.objects.all()
    return render(request,'galeria.html',{'object_list':object_list,'deptos':deptos,'tipo':tipo})    

def signup(request):  
    if request.method == 'GET' :
      return render(request,'signup.html',{
        'form' : UserCreationForm,
    })
    else:       
        if request.POST['password1'] == request.POST['password2']:            
            try:
                 #register user
                user = User.objects.create_user(username=request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(products)
                #return render(request,'tasks')
            except IntegrityError:   
                return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    'error':'El Usuario ya existe'
                }) 
        return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    'error':'Contreñas no coninciden'
                }) 


@login_required
def departamentos(request):
    dep = Departamento.objects.all()
    return render(request, 'departamentos.html',{'deptos':dep})

@login_required
def tipo_mercancia(request):
    tipo = TipoMercancia.objects.all()
    print(tipo)
    return render(request, 'tipo_mercancia.html',{'tipo':tipo})    

@login_required
def products(request):  
    prod = Producto.objects.all()
    deptos = Departamento.objects.all()
    tipo = TipoMercancia.objects.all()
    return render(request, 'products.html',{'products':prod,'deptos':deptos,'tipo':tipo}) 

@login_required
def product_detail(request,product_id) :   
    if request.method == 'GET': 
        product= get_object_or_404(Product,pk=product_id)       
        form= ProductForm(instance=product)
        return render(request,'product_detail.html',{'product':product,'form':form})
    else: 
        try: 
            product= get_object_or_404(Product,pk=product_id)
            form= ProductForm(request.POST,instance=product)
            form.save()
            return redirect('products')
        except ValueError:
            return render(request,'product_detail.html',{'product':product,'form':form, 'error': 'Error al actualizar el producto'})    

@login_required
def create_product(request):
    if request.method == 'GET':
        return render(request,'create_product.html',{
            'form':ProductForm
        }) 
    else : 
        try:
            form = ProductForm(request.POST)
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('products')
        except:   
            return render(request,'create_product.html',{
                'form':ProductForm,
                'error':'Por favor envie datos validos'
            }) 



def tasks(request):
    tasks = Task.objects.filter(user=request.user,datecompleted__isnull = True)
    return render(request, 'tasks.html',{'tasks':tasks})  

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user,datecompleted__isnull = False).order_by('-datecompleted')
    return render(request, 'tasks.html',{'tasks':tasks})  

@login_required
def task_detail(request,task_id) :   
    if request.method == 'GET': 
        task= get_object_or_404(Task,pk=task_id,user=request.user)       
        form= TaskForm(instance=task)
        return render(request,'task_Detail.html',{'task':task,'form':form})
    else: 
        try: 
            task= get_object_or_404(Task,pk=task_id, user=request.user)
            form= TaskForm(request.POST,instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'task_Detail.html',{'task':task,'form':form, 'error': 'Error al actualizar la tarea'})

@login_required
def complete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.delete()
        return redirect('tasks')

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')        

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html',{
            'form':TaskForm
        }) 
    else : 
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except:   
            return render(request,'create_task.html',{
                'form':TaskForm,
                'error':'Por favor envie datos validos'
            }) 

@login_required
def closesession(request):
    logout(request)
    return redirect(home)

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form': AuthenticationForm,
        })
    else:
        user =  authenticate(request,username= request.POST['username'],password= request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
            'form': AuthenticationForm,
            'error': 'El usuario o el password es incorrecto'
        }) 
        else:
            login(request, user)
            return redirect(products)

def guardarProducto(request):
  if request.method == "POST": 
    codigo=request.POST['codigo']   
    nombre=request.POST['nombre']
    det=request.POST['descripcion']
    #dep=request.POST['departamento']
    dep=Departamento.objects.get(id=request.POST["departamento"])
    tipo=TipoMercancia.objects.get(id=request.POST['tipoMercancia'])
    precio=request.POST['precio']
    imagen=request.FILES.getlist('images')  
    images = request.FILES.getlist('images')
    for image in images:
     imagen = image   
     print(dep)
    producto = Producto.objects.create(codigo=codigo,nombre=nombre,user =request.user,activo=True,producto_imagen = imagen,descripcion=det,departamento=dep,precio= precio,tipo=tipo )
    return redirect('products')

def guardarDepto(request):
        detalle=request.POST['nombre2']   
        nombre=request.POST['nombre']   
        depto = Departamento.objects.create(nombre=nombre,detalle=detalle,user =request.user,active=True)
        return redirect('departamentos')

def handleMultipleImagesUpload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')

        for image in images:
            gallery.objects.create(image = image)

    return render(request, "home.html")   


@login_required
def filtros_accordion(request):  
    deptos = Department.objects.all()
    tipo = TipoMercancia.objects.all()
    return render(request, 'products.html',{'products':prod,'deptos':deptos,'tipo':tipo})  

def guardarTipoMercancia(request):
        tipo=request.POST['tipo']   
        descripcion=request.POST['descripcion']   
        tipoM = TipoMercancia.objects.create(Tipo=tipo,descripcion=descripcion,user =request.user,activo=True)
        return redirect('tipo_mercancia')       


        


        

       



