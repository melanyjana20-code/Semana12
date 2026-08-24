# Aplicación Restaurante

Proyecto académico desarrollado en Python para aplicar Programación Orientada a Objetos, estructuras de datos, manejo de archivos JSON y manejo de excepciones.

La aplicación permite registrar, buscar, actualizar, eliminar y listar productos. También permite registrar usuarios, listarlos y mostrar las categorías de productos sin repetir. Los productos se conservan en un archivo JSON para que permanezcan disponibles después de cerrar y volver a ejecutar el programa.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

La carpeta `datos/` se utiliza para almacenar físicamente el archivo `productos.json`, encargado de conservar la información de los productos.

## Ejecución

Desde la carpeta `restaurante_app`, ejecutar:

```bash
python main.py
```

## Responsabilidades

- `modelos/producto.py`: contiene la clase `Producto`, sus atributos, validaciones y la conversión del objeto a una representación compatible con JSON.

- `modelos/usuario.py`: contiene la clase `Usuario` y sus datos principales.

- `servicios/restaurante.py`: administra las colecciones de productos y usuarios, además de las operaciones principales del sistema.

- `servicios/archivo_servicio.py`: se encarga de leer y escribir los productos en el archivo JSON utilizando `with open()`, `json.load()` y `json.dump()`.

- `main.py`: contiene el menú principal, crea los servicios, recupera los productos almacenados al iniciar y solicita el guardado cuando se registra, actualiza o elimina un producto.

## Persistencia con JSON

La aplicación utiliza el archivo `datos/productos.json` para conservar los productos registrados.

Al iniciar el programa, se realiza la lectura del archivo mediante `json.load()`. Cada registro recuperado se utiliza para reconstruir un objeto de la clase `Producto`, permitiendo que el sistema continúe trabajando con objetos.

Cuando se registra, actualiza o elimina un producto, la colección actual se convierte a una representación compatible con JSON y se guarda nuevamente mediante `json.dump()`.

### Flujo de carga

```text
Inicio de la aplicación
        |
Leer datos/productos.json
        |
Convertir registros a objetos Producto
        |
Cargar productos en el servicio Restaurante
        |
Ejecutar el menú principal
```

### Flujo de guardado

```text
Registrar, actualizar o eliminar producto
        |
Restaurante modifica la colección
        |
Producto se convierte a diccionario
        |
ArchivoServicio guarda la información
        |
Actualizar datos/productos.json
```

## Manejo de excepciones

El proyecto utiliza excepciones específicas para controlar posibles errores durante la lectura, escritura y recuperación de información.

- `FileNotFoundError`: permite iniciar el programa con una colección vacía cuando `productos.json` todavía no existe.

- `json.JSONDecodeError`: controla el caso en que el archivo existe, pero su contenido no tiene un formato JSON válido.

- `PermissionError`: informa cuando no existen permisos suficientes para leer o guardar el archivo.

- `KeyError`: controla registros que no contienen todos los campos necesarios para reconstruir un producto.

- `ValueError` y `TypeError`: permiten controlar datos con valores o tipos incorrectos.

No se utiliza `except: pass`, ya que los errores son tratados de manera específica.

## Uso de estructuras de datos

### Lista (`list`)

Se utiliza para almacenar las colecciones de productos y usuarios durante la ejecución.

La lista permite registrar, buscar, actualizar, eliminar y recorrer los objetos almacenados.

### Tupla (`tuple`)

Se utiliza para representar opciones o valores definidos que no necesitan modificarse durante la ejecución del programa.

### Diccionario (`dict`)

Se utiliza para representar temporalmente la información de un producto mediante pares de clave y valor.

Esta representación permite convertir los objetos `Producto` a un formato compatible con JSON sin reemplazar la clase `Producto`.

Ejemplo de representación:

```json
{
    "codigo": "P001",
    "nombre": "Hamburguesa",
    "categoria": "Comida",
    "precio": 4.5
}
```

### Conjunto (`set`)

Se utiliza para obtener las categorías de los productos sin elementos repetidos, permitiendo mostrar cada categoría una sola vez.

## Menú principal

El programa permite realizar las siguientes operaciones:

1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Listar usuarios
8. Mostrar categorías
9. Salir

## Comprobación de persistencia

Para comprobar el funcionamiento de la persistencia se realizaron las siguientes pruebas:

1. Se ejecutó `main.py`.
2. Se registró un producto desde el menú principal.
3. Se verificó que la información fuera almacenada en `datos/productos.json`.
4. Se cerró completamente el programa.
5. Se ejecutó nuevamente `main.py`.
6. Se utilizó la opción de listar productos y se comprobó que el producto registrado anteriormente fue recuperado.
7. Se actualizó la información del producto y se comprobó que el cambio permaneciera después de reiniciar el programa.
8. Se eliminó el producto y se volvió a ejecutar la aplicación.
9. Finalmente, se comprobó que el producto eliminado ya no aparecía y que `productos.json` contenía una lista vacía (`[]`).

De esta manera se comprobó que la aplicación mantiene correctamente la información de los productos entre diferentes ejecuciones.

## Objetivo pedagógico

Aplicar Programación Orientada a Objetos junto con estructuras de datos persistencia mediante archivos JSON y manejo específico de excepciones, manteniendo separadas las responsabilidades de los modelos, servicios, almacenamiento e interacción por consola.