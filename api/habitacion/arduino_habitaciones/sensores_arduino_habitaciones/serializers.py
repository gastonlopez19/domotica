from rest_framework import serializers
from api.habitacion.arduino_habitaciones.sensores_arduino_habitaciones.models import sensores_arduino_habitaciones

class sensores_arduino_habitacionesSerializers(serializers.ModelSerializer):
    id_sensor = serializers.CharField(source='id')

    class Meta:
        model = sensores_arduino_habitaciones
        fields = ('id_habitacion','id_arduino','id_sensor','estado_sensor','valor_sensor')



