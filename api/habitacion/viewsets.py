from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from api.habitacion.models import habitacion
from api.habitacion.serializers import HabitacionSerializer


class HabitacionViewSets(viewsets.ModelViewSet):
    queryset = habitacion.objects.all()
    serializer_class = HabitacionSerializer
    http_method_names = ['get','post','put','delete']
    permission_classes = ()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'descripcion']