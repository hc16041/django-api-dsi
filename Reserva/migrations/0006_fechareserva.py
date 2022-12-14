# Generated by Django 4.0.4 on 2022-11-02 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0002_habitacion_imagen_habitacion'),
        ('Reserva', '0005_rename_total_gasto_reserva_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='FechaReserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
                ('fecha_salida', models.DateField(verbose_name='Fecha de salida')),
                ('id_habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitacion.habitacion')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reserva.reserva')),
            ],
            options={
                'verbose_name': 'FechaReserva',
                'verbose_name_plural': 'FechasReserva',
            },
        ),
    ]
