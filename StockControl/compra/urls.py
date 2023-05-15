from django.urls import path
from compra import views


urlpatterns = [
    path("", views.home_view, name='Home'),
    path("proveedores/", views.proveedores_view, name='Lista-Proveedores'),
    path("proveedores/alta/", views.crear_proveedor, name='Crear-Proveedor'),
    
    path("productos/", views.productos_view, name='Lista-Productos'),
    path("productos/alta/", views.crear_producto, name='Crear-Producto'),
    
]