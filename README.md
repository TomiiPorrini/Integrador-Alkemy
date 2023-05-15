# Integrador-Alkemy

Construir una aplicación con Django para agregar nuevos clientes y poder listarlos.

# Cómo comenzar:
1. Clonar el repositorio e ir a la consola y colocar el siguiente comando:

```
    pip install -r requirements.txt
```

2. Cuando se termine de descargar el archivo requirements.txt, entonces ingresaremos a la carpeta con este comando:

```
    cd StockControl
```

3. Ahora, ejecutaremos el proyecto Django con el siguiente comando:

```
    py manage.py runserver
```

4. Listo, ya podes revisar todo lo que esta implementado en el programa.
> P/D: Intentá no romperlo 😅

## 📝 Requerimientos

Se pide crear un proyecto que podría ser llamado StockControl:

✓ Agregar una app llamada compra.

✓ Dentro de esta app se deben agregar los modelos Producto y Proveedor (ver más abajo los fields requeridos).

✓ El Producto debe estar relacionado con el Proveedor: entiéndase que un Proveedor es una foreignkey en Producto.

✓ Crear el archivo migration y ejecutarlo.

## 📝Acciones:

* Listar todos los productos registrados en la base de datos

* Permitir agregar un nuevo producto.

* Permitir agregar un nuevo proveedor.

* Tener disponible en el Admin el modelo del producto y del proveedor.

> La aplicación debe permitir almacenar nuevos productos y proveedores para luego mostrarlos en un listado.



## 🎁Bonus (no obligatorio)

* Implementar uso de Bootstrap en los HTMLs

* Generar el listado de Proveedores.

* Generar el archivo requirements del proyecto


### ‼ Para tener en cuenta  

Para poder ingresar en el Admin, los datos son:
* user: Admin
* psw: 1234
