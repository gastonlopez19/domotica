from rest_framework import viewsets
from api.habitacion.arduino_habitaciones.sensores_arduino_habitaciones.models import sensores_arduino_habitaciones
from api.habitacion.arduino_habitaciones.sensores_arduino_habitaciones.serializers import sensores_arduino_habitacionesSerializers
from django_filters.rest_framework import DjangoFilterBackend

class sensores_arduino_habitacionesViewSets(viewsets.ModelViewSet):
    queryset = sensores_arduino_habitaciones.objects.all()
    serializer_class = sensores_arduino_habitacionesSerializers
    http_method_names = ('get','post','put','delete')
    permission_classes = ()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'id_habitacion','id_arduino']

    