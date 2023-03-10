# Generated by Django 4.1.7 on 2023-03-06 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0027_alter_product_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('detalle', models.CharField(blank=True, max_length=200)),
                ('descripcion', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='tipomercancia',
            old_name='created',
            new_name='creado',
        ),
        migrations.RemoveField(
            model_name='tipomercancia',
            name='active',
        ),
        migrations.AddField(
            model_name='tipomercancia',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tipomercancia',
            name='descripcion',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default='123', max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=300)),
                ('precio', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
                ('producto_imagen', models.ImageField(default='', upload_to='images/')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.departamento')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.tipomercancia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
