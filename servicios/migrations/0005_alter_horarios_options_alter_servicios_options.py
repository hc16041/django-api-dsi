# Generated by Django 4.0.3 on 2022-08-28 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_servicios_capacidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horarios',
            options={'verbose_name': 'Horario', 'verbose_name_plural': 'Horarios'},
        ),
        migrations.AlterModelOptions(
            name='servicios',
            options={'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]