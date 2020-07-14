from rest_framework import serializers
from .models import arduino_habitaciones

class arduino_habitacionesSerializers(serializers.ModelSerializer):
    id_arduino =  serializers.CharField(source='id')
    class Meta:
        model = arduino_habitaciones
        fields = ('id_habitacion','id_arduino', 'descripcion')