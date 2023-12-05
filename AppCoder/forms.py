from django import forms
from .models import Clientes, Productos, Empleados
 
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre'] ## Acá agregás con coma y entre los corchetes el resto de campos
 
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion']

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre', 'puesto','legajo']