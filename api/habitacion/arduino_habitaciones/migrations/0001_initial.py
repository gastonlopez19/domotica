# Generated by Django 3.0.7 on 2020-07-28 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habitacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='arduino_habitaciones',
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
