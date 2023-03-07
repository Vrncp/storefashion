from django.contrib import admin
from .models import Task,TipoMercancia
from .models import Department, Product,gallery

# Register your models here.

admin.site.register(Task)
admin.site.register(Department)
admin.site.register(Product)
admin.site.register(gallery)
admin.site.register(TipoMercancia)
