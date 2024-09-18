from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['fotoUsuario1', 'fotoUsuario2', 'fotoUsuario3', 'fotoUsuario4', 'fotoUsuario5', 'fotoUsuario6']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer todos los campos de fotos obligatorios en el formulario de usuario
        for field in ['fotoUsuario1', 'fotoUsuario2', 'fotoUsuario3', 'fotoUsuario4', 'fotoUsuario5', 'fotoUsuario6']:
            self.fields[field].required = True