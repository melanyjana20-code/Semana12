import json
from typing import List

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    # ==============================
    # PRODUCTOS
    # ==============================

    @staticmethod
    def guardar_productos(
        ruta: str,
        productos: List[Producto]
    ) -> None:

        try:
            datos = [
                producto.convertir_a_diccionario()
                for producto in productos
            ]

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                "Error: no hay permisos para "
                "guardar productos."
            )

    @staticmethod
    def cargar_productos(
        ruta: str
    ) -> List[Producto]:

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            productos = []

            for dato in datos:

                try:
                    producto = Producto(
                        dato["codigo"],
                        dato["nombre"],
                        dato["categoria"],
                        float(dato["precio"]),
                        int(dato["stock"])
                    )

                    productos.append(producto)

                except KeyError as error:
                    print(
                        f"Error: falta la clave "
                        f"{error} en un producto."
                    )

                except ValueError as error:
                    print(
                        f"Error en los datos "
                        f"del producto: {error}"
                    )

            return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json contiene "
                "JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para "
                "leer productos."
            )
            return []

    # ==============================
    # USUARIOS
    # ==============================

    @staticmethod
    def guardar_usuarios(
        ruta: str,
        usuarios: List[Usuario]
    ) -> None:

        try:
            datos = [
                usuario.convertir_a_diccionario()
                for usuario in usuarios
            ]

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                "Error: no hay permisos para "
                "guardar usuarios."
            )

    @staticmethod
    def cargar_usuarios(
        ruta: str
    ) -> List[Usuario]:

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            usuarios = []

            for dato in datos:

                try:
                    usuario = Usuario(
                        dato["identificacion"],
                        dato["nombre"]
                    )

                    usuarios.append(usuario)

                except KeyError as error:
                    print(
                        f"Error: falta la clave "
                        f"{error} en un usuario."
                    )

                except ValueError as error:
                    print(
                        f"Error en los datos "
                        f"del usuario: {error}"
                    )

            return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: usuarios.json contiene "
                "JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para "
                "leer usuarios."
            )
            return []

    # ==============================
    # VENTAS
    # ==============================

    @staticmethod
    def guardar_ventas(
        ruta: str,
        ventas: List[Venta]
    ) -> None:

        try:
            datos = [
                venta.convertir_a_diccionario()
                for venta in ventas
            ]

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                "Error: no hay permisos para "
                "guardar ventas."
            )

    @staticmethod
    def cargar_ventas(
        ruta: str
    ) -> List[Venta]:

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            ventas = []

            for dato in datos:

                try:
                    venta = Venta(
                        dato["usuario_id"],
                        dato["producto_codigo"],
                        int(dato["cantidad"])
                    )

                    ventas.append(venta)

                except KeyError as error:
                    print(
                        f"Error: falta la clave "
                        f"{error} en una venta."
                    )

                except ValueError as error:
                    print(
                        f"Error en los datos "
                        f"de la venta: {error}"
                    )

            return ventas

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: ventas.json contiene "
                "JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para "
                "leer ventas."
            )
            return []