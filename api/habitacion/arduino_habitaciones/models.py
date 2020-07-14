from django.db import models
from api.habitacion.models import habitacion

class arduino_habitaciones(models.Model):
    
    id_habitacion = models.ForeignKey(habitacion, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.descripcion
    


    class Meta:
        verbose_name = 'arduino_Habitacion'
        verbose_name_plural = 'arduino_Habitaciones'