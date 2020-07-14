"""domotica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from api.habitacion.viewsets import HabitacionViewSets
from api.habitacion.arduino_habitaciones.viewsets import arduino_habitacionesViewSet
from api.habitacion.arduino_habitaciones.sensores_arduino_habitaciones.viewsets import sensores_arduino_habitacionesViewSets
from api.clima import views

router = routers.DefaultRouter()
router.register(r'Habitaciones',HabitacionViewSets)
router.register(r'Arduino_Habilitaciones',arduino_habitacionesViewSet)
router.register(r'Sensores_Arduino_Habitaciones',sensores_arduino_habitacionesViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('clima', views.clima.as_view())
]
