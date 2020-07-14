from django.db import models
from api.habitacion.models import habitacion
from api.habitacion.arduino_habitaciones.models import arduino_habitaciones


# Create your models here.
class sensores_arduino_habitaciones(models.Model):
    id_habitacion = models.ForeignKey(habitacion, on_delete=models.CASCADE) 
    id_arduino =  models.ForeignKey(arduino_habitaciones, on_delete=models.CASCADE) 
    estado_sensor = models.CharField( verbose_name="Estado Sensor", max_length=3)
    valor_sensor = models.CharField( verbose_name="Valor Sensor", max_length=3)

    class Meta:
        verbose_name = "sensores_arduino_habitacion"
        verbose_name_plural = "sensores_arduino_habitaciones"

  
   