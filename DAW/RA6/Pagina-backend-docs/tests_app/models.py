from django.db import models
from usuarios_app.models import Usuario

# Create your models here.
class Test(models.Model):
    """
    Modelo que representa un test.
    
    Atributos:
        - autor: Usuario que creó el test.
        - nombre: Nombre del test (único).
        - descripcion: Descripción opcional del test.
        - fecha_creacion: Fecha y hora en que se creó el test.
    """
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="tests", unique=False, null=False, blank=False)
    nombre = models.CharField(max_length=30, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=1000, unique=False, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, unique=False, null=False, blank=False)



class Pregunta(models.Model):
    """
    Modelo que representa una pregunta dentro de un test.
    
    Atributos:
        - test: Test al que pertenece la pregunta.
        - texto: Contenido de la pregunta.
    """
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="preguntas", unique=False, null=False, blank=False)
    texto = models.CharField(max_length=255, unique=False, null=False, blank=False)


"""
    Clase provisional...
"""
class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="respuestas", null=False, blank=False)
    texto = models.CharField(max_length=255, unique=False, null=False, blank=False)