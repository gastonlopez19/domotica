from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import coreapi

class clima(APIView):
    def get(self,request, format=None):
        client = coreapi.Client()
        schema = client.get("https://api.openweathermap.org/data/2.5/weather?q=Haedo&units=metric&appid=597b214f0dd1fe70ae83d981efc70f7a")
        return Response({"Ciudad": "Haedo","temperatura_actual":schema["main"]["temp"] ,"temperatura_minima": schema["main"]["temp_min"], "temperatura_maxima" :schema["main"]["temp_max"], "humedad" :schema["main"]["humidity"]  })


        