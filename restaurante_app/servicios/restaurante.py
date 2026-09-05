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

        # ==========================================
        # NUEVOS ÍNDICES PARA OPTIMIZAR BÚSQUEDAS
        # ==========================================

        # Índice de productos por código
        self._productos_por_codigo: dict[str, Producto] = {}

        # Índice de usuarios por identificación
        self._usuarios_por_identificacion: dict[str, Usuario] = {}

        # Índice de ventas por usuario
        self._ventas_por_usuario: dict[str, List[Venta]] = {}

        # Conjunto de categorías
        self._categorias: set[str] = set()

        # Reconstruir índices con los datos cargados
        self._reconstruir_indices()

    # ==========================================
    # RECONSTRUIR ÍNDICES
    # ==========================================

    def _reconstruir_indices(self) -> None:

        for producto in self._productos:
            self._productos_por_codigo[
                producto.codigo
            ] = producto

            self._categorias.add(
                producto.categoria
            )

        for usuario in self._usuarios:
            self._usuarios_por_identificacion[
                usuario.identificacion
            ] = usuario

        for venta in self._ventas:

            if venta.usuario_id not in self._ventas_por_usuario:
                self._ventas_por_usuario[
                    venta.usuario_id
                ] = []

            self._ventas_por_usuario[
                venta.usuario_id
            ].append(venta)

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

        # Agregar al índice
        self._productos_por_codigo[
            producto.codigo
        ] = producto

        # Agregar categoría al conjunto
        self._categorias.add(
            producto.categoria
        )

        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Optional[Producto]:

        # Búsqueda optimizada utilizando diccionario
        return self._productos_por_codigo.get(codigo)

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

        # Mantener actualizado el conjunto de categorías
        self._categorias.add(categoria)

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)

        # Eliminar del índice
        self._productos_por_codigo.pop(
            codigo,
            None
        )

        # Reconstruir categorías para evitar
        # conservar categorías que ya no existen
        self._categorias = {
            producto.categoria
            for producto in self._productos
        }

        return True

    def listar_productos(self) -> List[Producto]:

        return self._productos.copy()

    def obtener_categorias(self) -> set:

        return self._categorias.copy()

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

        # Agregar al índice
        self._usuarios_por_identificacion[
            usuario.identificacion
        ] = usuario

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Optional[Usuario]:

        # Búsqueda optimizada utilizando diccionario
        return self._usuarios_por_identificacion.get(
            identificacion
        )

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

        # Agregar venta al índice por usuario
        if usuario.identificacion not in self._ventas_por_usuario:
            self._ventas_por_usuario[
                usuario.identificacion
            ] = []

        self._ventas_por_usuario[
            usuario.identificacion
        ].append(venta)

        return True

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> List[Venta]:

        # Consulta optimizada mediante diccionario
        return self._ventas_por_usuario.get(
            identificacion_usuario,
            []
        ).copy()

    def listar_ventas(self) -> List[Venta]:

        return self._ventas.copy()