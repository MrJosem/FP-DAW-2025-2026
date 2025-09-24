from .models import Test, Pregunta, Respuesta
from django import forms

class TestForm(forms.ModelForm):
    """
    Formulario para la creación y edición de un Test.
    
    Campos:
        - nombre: Nombre del test.
        - descripcion: Descripción opcional del test.
    """
    class Meta:
        model = Test

        fields = [
            'nombre',
            'descripcion'
        ]
        exclude = ['usuario']
        widget = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ejemplo: Ansiedad'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Ejemplo: Este test está hecho para diagnosticar la ansiedad'})
        }


class PreguntaForm(forms.ModelForm):
    """
    Formulario para la creación y edición de una Pregunta dentro de un Test.
    
    Campos:
        - texto: Contenido de la pregunta.
    """
    class Meta:
        model = Pregunta

        fields = [
            'texto',
        ]
        exclude = ['usuario']
        widget = {
            'texto': forms.TextInput(attrs={'placeholder': 'Ejemplo: ¿Últimamente te sientes muy estresado?'}),
        }


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta

        fields = [
            'texto',
        ]
        exclude = ['usuario']
        widget = {
            'texto': forms.TextInput(attrs={'placeholder': 'Ejemplo: Estoy muy nervioso...'}),
        }