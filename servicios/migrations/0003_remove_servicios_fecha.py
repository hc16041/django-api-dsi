# Generated by Django 4.0.3 on 2022-05-27 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_remove_servicios_iva_horarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicios',
            name='fecha',
        ),
    ]
