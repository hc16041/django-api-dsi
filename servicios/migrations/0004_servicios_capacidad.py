# Generated by Django 4.0.3 on 2022-05-27 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_remove_servicios_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='capacidad',
            field=models.CharField(default='', max_length=50, verbose_name='Capacidad'),
        ),
    ]
