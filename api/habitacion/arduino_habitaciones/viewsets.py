from rest_framework import viewsets
from api.habitacion.arduino_habitaciones.serializers import arduino_habitacionesSerializers
from api.habitacion.arduino_habitaciones.models import arduino_habitaciones
from django_filters.rest_framework import DjangoFilterBackend


class arduino_habitacionesViewSet(viewsets.ModelViewSet):
    queryset = arduino_habitaciones.objects.all()
    serializer_class = arduino_habitacionesSerializers
    http_method_names = ('get','post','put','delete')
    permission_classes = ()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'id_habitacion','descripcion']


