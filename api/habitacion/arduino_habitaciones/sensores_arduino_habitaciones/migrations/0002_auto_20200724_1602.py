# Generated by Django 3.0.7 on 2020-07-24 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensores_arduino_habitaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensores_arduino_habitaciones',
            old_name='arduino',
            new_name='id_arduino',
        ),
        migrations.RenameField(
            model_name='sensores_arduino_habitaciones',
            old_name='habitacion',
            new_name='id_habitacion',
        ),
    ]
