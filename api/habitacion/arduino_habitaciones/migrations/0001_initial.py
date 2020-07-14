# Generated by Django 3.0.8 on 2020-07-11 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habitacion', '0003_auto_20200711_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arduino_Habitaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=1000)),
                ('id_habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitacion.habitacion')),
            ],
            options={
                'verbose_name': 'arduino_Habitacion',
                'verbose_name_plural': 'arduino_Habitaciones',
            },
        ),
    ]
