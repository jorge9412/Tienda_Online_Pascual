from django import forms
from inventario.models import Productos

class DocumentoForm(forms.Form):
    class Meta:
        model = Productos
        fields = ('name', 'category','cost','cantidad_stock','description', 'imagen',)