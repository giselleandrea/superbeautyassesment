from django.urls import path
from .views import ListaEquiposAPIView

urlpatterns = [
    #Ruta para acceder a la API que devuelve la lista de equipos
    path('api/lista-equipos/', ListaEquiposAPIView.as_view(), name='lista_equipos_api'),
]

