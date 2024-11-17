from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios, TiposUsuarios, Solicitudes

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

class SolicitudEncargoForm(forms.ModelForm):
    archivo_stl = forms.FileField(label='Archivo STL (hasta 80 MB)', required=True)

    class Meta:
        model = Solicitudes
        fields = ['archivo_stl', 'material_id', 'dimensiones', 'ubicacion_entrega']

    def clean_archivo_stl(self):
        archivo = self.cleaned_data.get('archivo_stl')
        if archivo:
            if archivo.size > 80 * 1024 * 1024:
                raise forms.ValidationError("El archivo STL no puede exceder los 80 MB.")
            if not archivo.name.endswith('.stl'):
                raise forms.ValidationError("El archivo debe ser en formato STL.")
        return archivo