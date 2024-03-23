from django.db import models
from django.contrib.auth.models import User

# Modelo Equipo
"""
Registra datos basicos para un inventario de computadores
"""
class Equipo(models.Model):
    referencia = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    memoria = models.CharField(max_length=100)
    disco = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        """
        Devuelve un String del objeto Equipo.
        Returns:
            str: Referencia del equipo.
        """
        return self.referencia

#Modelo EquipoUsuario
"""
Establece una relación etre el modelo equipo y los usuarios de Django debido al uso de SQLite3  
"""    
class EquipoUsuario(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    fecha_entrega = models.DateField()

    def __str__(self):
        """
        Devuelve un String del objeto EquipoUsuario.
        Returns:
            str: String formateado que incluye la referencia del 
                equipo asignado y el nombre de usuario al que está asignado.
        """
        return f"{self.equipo} asignado: {self.usuario.username}"