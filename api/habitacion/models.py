from django.db import models

# Create your models here.
class habitacion(models.Model):
    descripcion = models.CharField( max_length=1000)    

    def __str__(self):
        return self.descripcion
    


    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
    
    