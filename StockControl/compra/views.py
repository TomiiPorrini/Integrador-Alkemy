from django.shortcuts import render, redirect
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def proveedores_view(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listaProveedores.html', context={'proveedores':proveedores})

def productos_view(request):
    productos = Producto.objects.all()
    return render(request, 'listaProductos.html', context={'productos':productos})

def crear_producto(request):
    form = ProductoForm()
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista-Productos')
        else:
            return redirect('Lista-Productos')
    
    return render(request, 'crear_producto.html', {'form': form})

def crear_proveedor(request):
    form = ProveedorForm()
    
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista-Proveedores')
            
        else:
            print("quedaron campos vacios ")
            return redirect('Lista-Proveedores')
    
    return render(request, 'crear_proveedor.html', {'form': form})