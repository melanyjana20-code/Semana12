from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario

from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


def mostrar_menu(restaurante: Restaurante) -> None:
    print("\n==================================")
    print(" SISTEMA DE RESTAURANTE")
    print("==================================")

    for numero, opcion in enumerate(
        restaurante.opciones_menu,
        start=1
    ):
        print(f"{numero}. {opcion}")

    print("==================================")


def guardar_productos(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    productos = restaurante.obtener_productos()

    archivo_servicio.guardar_productos(productos)


def ejecutar_sistema() -> None:
    restaurante = Restaurante()

    # Ruta segura hacia la carpeta del proyecto
    ruta_base = Path(__file__).resolve().parent

    ruta_productos = (
        ruta_base
        / "datos"
        / "productos.json"
    )

    archivo_servicio = ArchivoServicio(
        str(ruta_productos)
    )

    productos_guardados = (
        archivo_servicio.cargar_productos()
    )

    restaurante.cargar_productos(
        productos_guardados
    )

    while True:
        mostrar_menu(restaurante)

        opcion = input(
            "Seleccione una opción (1-9): "
        ).strip()

        if opcion == "1":
            print("\n--- REGISTRAR PRODUCTO ---")

            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()

            try:
                precio = float(
                    input("Precio: ").strip()
                )

                producto = Producto(
                    codigo,
                    nombre,
                    categoria,
                    precio
                )

                registrado = (
                    restaurante.registrar_producto(
                        producto
                    )
                )

                if registrado:
                    guardar_productos(
                        restaurante,
                        archivo_servicio
                    )

            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            print("\n--- BUSCAR PRODUCTO ---")

            codigo = input(
                "Ingrese el código del producto: "
            ).strip()

            producto = restaurante.buscar_producto(
                codigo
            )

            if producto is None:
                print("Producto no encontrado.")

            else:
                print(
                    producto.mostrar_informacion()
                )

        elif opcion == "3":
            print("\n--- ACTUALIZAR PRODUCTO ---")

            codigo = input(
                "Código del producto: "
            ).strip()

            producto = restaurante.buscar_producto(
                codigo
            )

            if producto is None:
                print("Producto no encontrado.")
                continue

            nombre = input(
                "Nuevo nombre: "
            ).strip()

            categoria = input(
                "Nueva categoría: "
            ).strip()

            try:
                precio = float(
                    input("Nuevo precio: ").strip()
                )

                actualizado = (
                    restaurante.actualizar_producto(
                        codigo,
                        nombre,
                        categoria,
                        precio
                    )
                )

                if actualizado:
                    guardar_productos(
                        restaurante,
                        archivo_servicio
                    )

            except ValueError:
                print(
                    "Error: el precio debe ser "
                    "un número válido."
                )

        elif opcion == "4":
            print("\n--- ELIMINAR PRODUCTO ---")

            codigo = input(
                "Código del producto: "
            ).strip()

            eliminado = (
                restaurante.eliminar_producto(
                    codigo
                )
            )

            if eliminado:
                guardar_productos(
                    restaurante,
                    archivo_servicio
                )

        elif opcion == "5":
            restaurante.listar_productos()

        elif opcion == "6":
            print("\n--- REGISTRAR USUARIO ---")

            identificacion = input(
                "Identificación: "
            ).strip()

            nombre = input(
                "Nombre completo: "
            ).strip()

            correo = input(
                "Correo electrónico: "
            ).strip()

            usuario = Usuario(
                identificacion,
                nombre,
                correo
            )

            restaurante.registrar_usuario(
                usuario
            )

        elif opcion == "7":
            restaurante.listar_usuarios()

        elif opcion == "8":
            restaurante.mostrar_categorias()

        elif opcion == "9":
            print(
                "\nGracias por utilizar el sistema."
            )
            break

        else:
            print(
                "Opción no válida. "
                "Ingrese un número del 1 al 9."
            )


if __name__ == "__main__":
    ejecutar_sistema()