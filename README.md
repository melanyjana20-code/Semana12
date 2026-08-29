# Restaurante App - Semana 11

**Estudiante:** Melany Jaña

## Descripción

Aplicación académica desarrollada en Python para la asignatura Programación Orientada a Objetos.

El proyecto corresponde a la evolución de la aplicación `restaurante_app` desarrollada durante la Semana 10.

En esta Semana 11 se incorporan colecciones de objetos, relaciones entre Usuario y Producto mediante la entidad Venta, control de stock y persistencia JSON de productos, usuarios y ventas.

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
└── main.py
```

## Componentes

### Producto

La clase `Producto` representa los productos disponibles en el restaurante.

Contiene:

-   Código.
-   Nombre.
-   Categoría.
-   Precio.
-   Stock.

El stock no puede ser negativo y se reduce cuando se realiza una venta válida.

### Usuario

La clase `Usuario` representa a las personas registradas en el sistema.

Contiene:

-   Identificación.
-   Nombre.

Los usuarios se almacenan y recuperan mediante el archivo `usuarios.json`.

### Venta

La clase `Venta` representa la relación entre un usuario y un producto vendido.

Contiene:

-   Identificación del usuario.
-   Código del producto.
-   Cantidad vendida.

### Restaurante

La clase `Restaurante` administra las colecciones de:

-   Productos.
-   Usuarios.
-   Ventas.

También contiene las reglas principales del sistema, como registrar, buscar, actualizar, eliminar y vender productos.

### ArchivoServicio

La clase `ArchivoServicio` administra la persistencia de información mediante archivos JSON.

Utiliza:

-   `json.dump()`
-   `json.load()`
-   `with open()`
-   Codificación UTF-8.

## Relación Usuario - Producto - Venta

Para realizar una venta se verifica primero que exista el usuario y que exista el producto.

Después se valida que la cantidad sea mayor que cero y que exista suficiente stock.

Si todas las condiciones son correctas:

1.  Se crea un objeto `Venta`.
2.  La venta se agrega a la colección de ventas.
3.  Se disminuye el stock del producto.
4.  Se guarda `ventas.json`.
5.  Se guarda `productos.json`.

## Persistencia

La aplicación utiliza tres archivos JSON:

### productos.json

Conserva los productos registrados y su stock actualizado.

### usuarios.json

Conserva los usuarios registrados.

### ventas.json

Conserva las ventas realizadas y la relación entre usuarios y productos.

Al iniciar el programa, los archivos JSON son leídos y sus registros son reconstruidos nuevamente como objetos.

## Manejo de excepciones

Se controlan excepciones específicas:

-   `FileNotFoundError`: permite iniciar con una colección vacía si un archivo todavía no existe.
-   `json.JSONDecodeError`: controla archivos JSON inválidos.
-   `PermissionError`: controla problemas de permisos.
-   `KeyError`: controla claves faltantes en registros JSON.
-   `ValueError`: controla datos inválidos y validaciones de los modelos.

No se utiliza `except: pass`.

## Ejecución

Desde la carpeta `restaurante_app` ejecutar:

```
python main.py
```

## Operaciones disponibles

1.  Registrar producto.
2.  Buscar producto.
3.  Actualizar producto.
4.  Eliminar producto.
5.  Listar productos.
6.  Registrar usuario.
7.  Listar usuarios.
8.  Mostrar categorías.
9.  Realizar venta.
10.  Consultar ventas de un usuario.
11.  Listar ventas.
12.  Salir.

## Pruebas realizadas

Se realizaron pruebas de:

1.  Registro de productos con stock.
2.  Registro de usuarios.
3.  Realización de una venta válida.
4.  Verificación de disminución del stock.
5.  Verificación de la venta registrada en `ventas.json`.
6.  Verificación del nuevo stock en `productos.json`.
7.  Consulta de ventas por usuario.
8.  Cierre y reinicio del programa.
9.  Recuperación de productos, usuarios y ventas desde los archivos JSON.
10.  Intento de realizar una venta con una cantidad mayor al stock disponible.
11.  Verificación de que una venta inválida no modifica el stock.
12.  Validación de cantidades menores o iguales a cero.

## Objetivo

Aplicar los fundamentos de Programación Orientada a Objetos, colecciones, relaciones entre objetos, persistencia mediante archivos JSON y manejo específico de excepciones dentro de una aplicación de restaurante.