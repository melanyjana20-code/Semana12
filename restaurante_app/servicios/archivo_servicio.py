import json
from modelos.producto import Producto


class ArchivoServicio:
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo

    def guardar_productos(self, productos: list[Producto]) -> bool:
        datos = []

        for producto in productos:
            datos.append(producto.a_diccionario())

        try:
            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except PermissionError:
            print("Error: no se tienen permisos para guardar el archivo.")
            return False

    def cargar_productos(self) -> list[Producto]:
        productos = []

        try:
            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            if not isinstance(datos, list):
                print(
                    "Error: el contenido de productos.json "
                    "debe ser una lista."
                )
                return []

            for registro in datos:
                try:
                    producto = Producto(
                        codigo=registro["codigo"],
                        nombre=registro["nombre"],
                        categoria=registro["categoria"],
                        precio=float(registro["precio"])
                    )

                    productos.append(producto)

                except KeyError:
                    print(
                        "Advertencia: se encontró un registro "
                        "con información incompleta."
                    )

                except (ValueError, TypeError):
                    print(
                        "Advertencia: se encontró un registro "
                        "con información inválida."
                    )

            return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json no contiene "
                "un formato JSON válido."
            )
            return []

        except PermissionError:
            print(
                "Error: no se tienen permisos para leer "
                "productos.json."
            )
            return []