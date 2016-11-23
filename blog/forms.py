from django import forms
from .models import Cursos, Alumnos, Boleta
from django.contrib.auth.models import User

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('nombre','apellidos',)
class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields =('nombrecursos',)
class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields =('calificaciones','Alumno','Curso','fecha_publicacion',)
        widgets = {
            'Alumno':forms.SelectMultiple,
            'Curso': forms.Select,
}
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','groups')
        widgets = {
            'password':forms.PasswordInput,
            'groups': forms.SelectMultiple,
        }
