from typing import List, Optional

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self):
        # LISTAS: almacenan colecciones dinámicas
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []

        # TUPLA: información estable del sistema
        self.opciones_menu = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar usuario",
            "Listar usuarios",
            "Mostrar categorías",
            "Salir"
        )

        # DICCIONARIO: relación clave - valor
        self.descripcion_opciones = {
            1: "Registrar un nuevo producto",
            2: "Buscar producto por código",
            3: "Actualizar información de un producto",
            4: "Eliminar producto por código",
            5: "Mostrar todos los productos",
            6: "Registrar un nuevo usuario",
            7: "Mostrar todos los usuarios",
            8: "Mostrar categorías únicas",
            9: "Salir del sistema"
        }

    def cargar_productos(
        self,
        productos: List[Producto]
    ) -> None:
        self.productos = productos

    def obtener_productos(self) -> List[Producto]:
        return list(self.productos)

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        if self.buscar_producto(producto.codigo) is not None:
            print(
                "Error: ya existe un producto "
                "con ese código."
            )
            return False

        self.productos.append(producto)

        print("Producto registrado correctamente.")
        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Optional[Producto]:

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        if not nombre.strip():
            print("Error: el nombre no puede estar vacío.")
            return False

        if not categoria.strip():
            print("Error: la categoría no puede estar vacía.")
            return False

        if precio < 0:
            print("Error: el precio no puede ser negativo.")
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        print("Producto actualizado correctamente.")
        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
            return False

        self.productos.remove(producto)

        print("Producto eliminado correctamente.")
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados.")
            return

        print("\n--- LISTA DE PRODUCTOS ---")

        for producto in self.productos:
            print(producto.mostrar_informacion())

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:

        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.identificacion
                == usuario.identificacion
            ):
                print(
                    "Error: ya existe un usuario "
                    "con esa identificación."
                )
                return False

        self.usuarios.append(usuario)

        print("Usuario registrado correctamente.")
        return True

    def listar_usuarios(self) -> None:
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        print("\n--- LISTA DE USUARIOS ---")

        for usuario in self.usuarios:
            print(usuario.mostrar_informacion())

    def obtener_categorias(self) -> set[str]:
        # CONJUNTO: evita categorías duplicadas
        categorias = set()

        for producto in self.productos:
            categorias.add(producto.categoria)

        return categorias

    def mostrar_categorias(self) -> None:
        categorias = self.obtener_categorias()

        if not categorias:
            print("No hay categorías registradas.")
            return

        print("\n--- CATEGORÍAS ---")

        for categoria in sorted(categorias):
            print(categoria)