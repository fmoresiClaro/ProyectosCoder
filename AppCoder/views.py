from django.shortcuts import render, redirect
from .models import Clientes, Productos, Empleados
from .forms import ClientesForm, ProductosForm, EmpleadosForm
 
def AgregarClientes(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AgregarClientes')
    else:
        form = ClientesForm()
    return render(request, 'AgregarClientes.html', {'form': form})
 
def AgregarProductos(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AgregarProductos')
    else:
        form = ProductosForm()
    return render(request, 'AgregarProductos.html', {'form': form})

def AgregarEmpleados(request):
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AgregarEmpleados')
    else:
        form = EmpleadosForm()
    return render(request, 'AgregarEmpleados.html', {'form': form})
 
 
def buscar(request):
    if request.method == 'POST':
        term = request.POST.get('termino_busqueda')
        productos = Productos.objects.filter(nombre__icontains=term)
        return render(request, 'buscar.html', {'productos': productos})
    return render(request, 'buscar.html')

