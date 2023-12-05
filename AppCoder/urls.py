from django.urls import path
from .views import AgregarClientes, AgregarProductos, buscar, AgregarEmpleados
 
urlpatterns = [
    path('AgregarClientes/', AgregarClientes, name='AgregarClientes'),
    path('AgregarProductos/', AgregarProductos, name='AgregarProductos'),
    path('buscarProducto/', buscar, name='buscarProducto'),
    path('AgregarEmpleados/', AgregarEmpleados, name='AgregarEmpleados'),
]