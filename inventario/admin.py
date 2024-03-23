from django.contrib import admin
from .models import Equipo, EquipoUsuario

#Registro de modelos para el panel de administración de Django
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    """
    Clase para personalizar la visualización y el comportamiento 
    del modelo Equipo en el administrador.
    """
    #Lista los campos en la vista de lista de objetos del modelo Equipo
    list_display = ('id', 'referencia', 'marca', 'tipo')
    #Filtra por tipo
    list_filter = ('tipo',)
    #Busca por referencia.
    search_fields = ('referencia',)

@admin.register(EquipoUsuario)
class EquipoUsuarioAdmin(admin.ModelAdmin):
    """
    Clase para personalizar la visualización y el comportamiento 
    del modelo EquipoUsuario en el administrdor.
    """
    #Lista los campos en la vista de lista de objetos del modelo Equipousuario
    list_display = ('id', 'equipo', 'usuario', 'fecha_asignacion')
    #Filtra por fecha y por usuario
    list_filter = ('fecha_asignacion', 'usuario')    