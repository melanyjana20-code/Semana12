from typing import List, Optional

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:

    def __init__(
        self,
        productos: Optional[List[Producto]] = None,
        usuarios: Optional[List[Usuario]] = None,
        ventas: Optional[List[Venta]] = None
    ):
        self._productos = (
            productos if productos is not None else []
        )

        self._usuarios = (
            usuarios if usuarios is not None else []
        )

        self._ventas = (
            ventas if ventas is not None else []
        )

    # ==============================
    # PRODUCTOS
    # ==============================

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)

        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Optional[Producto]:

        for producto in self._productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.actualizar(
            nombre,
            categoria,
            precio,
            stock
        )

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)

        return True

    def listar_productos(self) -> List[Producto]:

        return self._productos.copy()

    def obtener_categorias(self) -> set:

        return {
            producto.categoria
            for producto in self._productos
        }

    # ==============================
    # USUARIOS
    # ==============================

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:

        if self.buscar_usuario(
            usuario.identificacion
        ) is not None:

            return False

        self._usuarios.append(usuario)

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Optional[Usuario]:

        for usuario in self._usuarios:

            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> List[Usuario]:

        return self._usuarios.copy()

    # ==============================
    # VENTAS
    # ==============================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None:
            return False

        if producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        producto.vender(cantidad)

        return True

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> List[Venta]:

        ventas_usuario: List[Venta] = []

        for venta in self._ventas:

            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> List[Venta]:

        return self._ventas.copy()