# Generated by Django 4.0.3 on 2022-05-27 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='imagen_habitacion',
            field=models.ImageField(default=' ', upload_to=None, verbose_name='Imagen de Habitación'),
        ),
    ]