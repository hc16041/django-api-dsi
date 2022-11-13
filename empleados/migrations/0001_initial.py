# Generated by Django 4.0.3 on 2022-05-25 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre_cargo', models.CharField(max_length=50, unique=True, verbose_name='Nombre de Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre_departamento', models.CharField(max_length=50, unique=True, verbose_name='Nombre de Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('nacionalidad', models.CharField(max_length=50, verbose_name='Nacionalidad')),
                ('dui', models.IntegerField(unique=True, verbose_name='DUI')),
                ('isss', models.IntegerField(unique=True, verbose_name='Numero de Afiliado')),
                ('nup', models.IntegerField(unique=True, verbose_name='Numero de Pensionado')),
                ('direccion', models.TextField(max_length=400, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo')),
                ('email', models.EmailField(default='email', max_length=254, verbose_name='Email')),
                ('fecha_contratacion', models.DateField(verbose_name='Fecha de Contratacion')),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.cargo', verbose_name='Cargo')),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
