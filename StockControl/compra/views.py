from django.shortcuts import render
from .models import Producto, Proveedor

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def proveedores_view(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listaProveedores.html', context={'proveedores':proveedores})

def productos_view(request):
    productos = Producto.objects.all()
    return render(request, 'listaProductos.html', context={'productos':productos})