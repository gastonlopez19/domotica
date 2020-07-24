from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

import coreapi

class clima(APIView):
    def get(self,request, format=None):
        client = coreapi.Client()
        fecha_hora = datetime.now()
        fecha_hora_string = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")




        ciudad = request.GET.get('ciudad')
        schema = client.get("https://api.openweathermap.org/data/2.5/weather?q=" +  ciudad +  "&units=metric&appid=597b214f0dd1fe70ae83d981efc70f7a")
        return Response({"Ciudad": ciudad,"temperatura_actual":schema["main"]["temp"] ,"temperatura_minima": schema["main"]["temp_min"], "temperatura_maxima" :schema["main"]["temp_max"], "humedad" :schema["main"]["humidity"], "fecha_hora" :  fecha_hora_string })


        