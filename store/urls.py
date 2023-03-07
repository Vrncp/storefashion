"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('menu/', views.menu,name='menu'),
    path('departamentos/', views.departamentos,name='departamentos'),
    path('tipo_mercancia/', views.tipo_mercancia,name='tipo_mercancia'),
    path('products/', views.products,name='products'),
    path('guardarProducto/', views.guardarProducto,name='guardarProducto'),
    path('guardarTipoMercancia/', views.guardarTipoMercancia,name='guardarTipoMercancia'),
    path('guardarDepto/', views.guardarDepto,name='guardarDepto'),
    path('products_completed/', views.tasks_completed,name='product_completed'),
    path('products/create/', views.create_product,name='create_product'),
    path('product/<int:product_id>/', views.product_detail,name='product_detail'),
    path('products/<int:product_id>/complete', views.complete_task,name='complete_products'),
    path('products/<int:product_id>/delete', views.delete_task,name='delete_task'), 
    path('tasks/', views.tasks,name='tasks'),
    #path('deptos/', views.deptos,name='deptos'),
    path('tasks_completed/', views.tasks_completed,name='tasks_completed'),
    path('tasks/create/', views.create_task,name='create_task'),
    path('task/<int:task_id>/', views.task_detail,name='task_detail'),
    path('task/<int:task_id>/complete', views.complete_task,name='complete_task'),
    path('task/<int:task_id>/delete', views.delete_task,name='delete_task'), 
    path('logout/', views.closesession,name='close'),
    path('galeria/', views.galeria,name='galeria'),
    path('upload/', views.handleMultipleImagesUpload, name="home"),
    path('signin', views.signin,name='signin')
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)