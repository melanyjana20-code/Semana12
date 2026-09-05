# Restaurante App

**Estudiante:** Melany Jaña

Aplicación académica de consola desarrollada en Python para practicar Programación Orientada a Objetos, colecciones, relaciones entre objetos, persistencia con archivos JSON y optimización de búsquedas.

El proyecto corresponde a la evolución de `restaurante_app` de la Semana 11. En esta Semana 12 se mantienen las funcionalidades anteriores y se incorporan índices internos con `dict` y `set` para mejorar búsquedas y consultas frecuentes.

## Estructura

    restaurante_app/
    │
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

## Componentes

- `modelos/`: contiene las clases principales del sistema.
- `servicios/`: contiene las reglas de negocio, persistencia e índices de búsqueda.
- `datos/`: contiene los archivos JSON de productos, usuarios y ventas.
- `main.py`: contiene el menú de consola y la entrada de datos.

## Mejora de la Semana 12

Se mantienen las listas de objetos utilizadas en la Semana 11 y se agregan colecciones auxiliares para mejorar el rendimiento de las búsquedas.

Se utilizan:

- `dict[str, Producto]`: búsqueda rápida de productos por código.
- `dict[str, Usuario]`: búsqueda rápida de usuarios por identificación.
- `dict[str, list[Venta]]`: consulta de ventas por usuario.
- `set[str]`: control de categorías únicas.

Estas mejoras son internas y no modifican el menú principal de la aplicación.

## Stock

Cada producto tiene un atributo `stock`.

Antes de realizar una venta se verifica:

- Que exista el producto.
- Que exista el usuario.
- Que la cantidad sea mayor que cero.
- Que exista suficiente stock.

Cuando la venta es válida, el stock del producto disminuye y nunca puede quedar en un valor negativo.

## Relación Usuario - Producto - Venta

La clase `Venta` relaciona un usuario con un producto mediante:

- Identificación del usuario.
- Código del producto.
- Cantidad vendida.

La venta permite relacionar los objetos `Usuario` y `Producto` sin modificar directamente sus modelos.

## Persistencia

La información se almacena en archivos JSON:

- `productos.json`: productos y stock.
- `usuarios.json`: usuarios registrados.
- `ventas.json`: ventas realizadas.

Para la persistencia se utilizan:

- `json.dump()`
- `json.load()`
- `with open()`
- Codificación UTF-8.

Al iniciar el programa, la información almacenada se carga nuevamente y se reconstruyen los objetos.

## Manejo de excepciones

El programa controla diferentes errores mediante excepciones específicas:

- `FileNotFoundError`
- `json.JSONDecodeError`
- `PermissionError`
- `KeyError`
- `ValueError`

No se utiliza `except: pass`.

## Operaciones principales

- Registrar productos.
- Buscar productos.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Listar usuarios.
- Mostrar categorías.
- Realizar ventas.
- Consultar ventas por usuario.
- Listar ventas.

## Ejecución

Para ejecutar el programa se debe ingresar a la carpeta `restaurante_app` y ejecutar:

    python main.py

## Pruebas realizadas

Se realizaron pruebas de:

- Registro de productos.
- Registro de usuarios.
- Ventas válidas.
- Disminución del stock.
- Ventas con stock insuficiente.
- Cantidades inválidas.
- Consulta de ventas por usuario.
- Consulta de categorías.
- Persistencia de productos, usuarios y ventas.
- Recuperación de la información después de reiniciar el programa.

## Objetivo

El objetivo del proyecto es aplicar Programación Orientada a Objetos, manejo de colecciones, relaciones entre objetos, persistencia de información mediante archivos JSON y optimización de búsquedas utilizando estructuras como `dict` y `set`.