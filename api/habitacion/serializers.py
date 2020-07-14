from rest_framework import serializers
from api.habitacion.models import habitacion

class HabitacionSerializer(serializers.ModelSerializer):
    id_habitacion = serializers.CharField(source="id")
    class Meta:
        model = habitacion
        fields = ('id_habitacion','descripcion')
