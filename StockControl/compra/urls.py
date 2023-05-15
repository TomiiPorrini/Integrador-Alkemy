from django.urls import path
from compra import views


urlpatterns = [
    path("", views.home_view, name='Home'),
    path("proveedores/", views.proveedores_view, name='Lista-Proveedores'),
    path("productos/", views.productos_view, name='Lista-Productos'),
    
]