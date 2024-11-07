from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios, TiposUsuarios

class RegistroForm(UserCreationForm):
    tipo_usuario = forms.ModelChoiceField(
        queryset=TiposUsuarios.objects.all(),
        required=True,
        label="Tipo de Usuario",
        empty_label="Seleccione un tipo de usuario",
        to_field_name="descripcion"  # Mostrar la descripción en lugar del ID
    )

    class Meta:
        model = Usuarios
        fields = ['nombre', 'email', 'direccion', 'tipo_usuario', 'password1', 'password2']
