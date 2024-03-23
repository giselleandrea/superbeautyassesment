from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Equipo, EquipoUsuario


class ListaEquiposAPIView(APIView):
    """
    Clase de vista para la API que devuelve la lista de equipos disponibles.
    """
    #Renderiza para visualizar los datos en formato JSON 
    renderer_classes = [JSONRenderer] 
    def get(self, request):
        """
        Método GET obtiene la lista de equipos disponibles.        
        Returns:
            Response: Respuesta HTTP con los datos de los equipos disponibles en formato JSON.
        """        
        #Obtiene los IDs de los equipos asignados
        equipos_asignados = EquipoUsuario.objects.values_list('equipo_id', flat=True)
        #Obtiene los equipos que no están asignados a ningún usuario 
        equipos_disponibles = Equipo.objects.exclude(id__in=equipos_asignados) 
        #equipos = Equipo.objects.all()
        #Crea una lista con los datos de los equipos disponibles
        data = [{
                'id': equipo.id, 
                'referencia': equipo.referencia, 
                'marca': equipo.marca, 
                'procesador': equipo.procesador, 
                'memoria': equipo.memoria, 
                'disco': equipo.disco, 
                'tipo': equipo.tipo 
            } for equipo in equipos_disponibles]
        #} for equipo in equipos]
        #Respuesta con los datos en formato JSON.
        return Response(data)

