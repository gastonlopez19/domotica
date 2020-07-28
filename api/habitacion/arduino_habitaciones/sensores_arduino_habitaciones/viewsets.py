#from rest_framework import status,viewsets

from rest_framework.views import APIView
from api.habitacion.arduino_habitaciones.sensores_arduino_habitaciones.models import sensores_arduino_habitaciones
from api.habitacion.arduino_habitaciones.sensores_arduino_habitaciones.serializers import sensores_arduino_habitacionesSerializers
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response


class sensores_arduino_habitacionesViewSets(APIView):


    def get(self,request):
        if request.GET.get("id_sensor") :
            sensores = sensores_arduino_habitacionesSerializers(sensores_arduino_habitaciones.objects.filter(id=request.GET.get("id_sensor")),many=True)

            return Response(sensores.data)

        else:
            sensores = sensores_arduino_habitacionesSerializers(sensores_arduino_habitaciones.objects.all(), many=True)
            return Response(sensores.data)


    def post(self,request):
        serializer = sensores_arduino_habitacionesSerializers (data=request.data)
        sensor = request.data
        if serializer.is_valid():
            serializer.save()
            return Response({"Estado": "Se ha almacenado correctamente"})
        else:
            return Response({"Estado": "No se ha almacenado correctamente"}) 
    

    def patch(self,request,pk=None):
        sensor = sensores_arduino_habitaciones.objects.filter(id=request.GET["id_sensor"]).get()
        serializer = sensores_arduino_habitacionesSerializers(sensor,request.data, partial=True)
        if sensor and serializer.is_valid():
            serializer.save()
            return Response({"Estado" :  "Se ha modificado correctamente"})
        else:
            return Response({"Estado" :  "No se ha modificado correctamente"})

    def delete(self,request,pk=None):
        sensor = sensores_arduino_habitaciones.objects.filter(id=request.GET["id_sensor"])
        if sensor :
            sensor.delete()
            return Response({"Estado": "Se ha eliminado correctamente"})
        else:
            return Response({"Estado": "No se ha podido eliminar"})
