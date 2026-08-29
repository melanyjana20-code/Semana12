from modelos.producto import Producto
from modelos.usuario import Usuario

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


RUTA_PRODUCTOS = "datos/productos.json"
RUTA_USUARIOS = "datos/usuarios.json"
RUTA_VENTAS = "datos/ventas.json"


def mostrar_menu() -> None:

    print("\n")
    print("========================================")
    print("          RESTAURANTE APP")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Mostrar categorías")
    print("9. Realizar venta")
    print("10. Consultar ventas de un usuario")
    print("11. Listar ventas")
    print("12. Salir")
    print("========================================")


def main() -> None:

    productos = ArchivoServicio.cargar_productos(
        RUTA_PRODUCTOS
    )

    usuarios = ArchivoServicio.cargar_usuarios(
        RUTA_USUARIOS
    )

    ventas = ArchivoServicio.cargar_ventas(
        RUTA_VENTAS
    )

    restaurante = Restaurante(
        productos,
        usuarios,
        ventas
    )

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        # ==================================
        # 1. REGISTRAR PRODUCTO
        # ==================================

        if opcion == "1":

            try:

                codigo = input(
                    "Código: "
                ).strip()

                nombre = input(
                    "Nombre: "
                ).strip()

                categoria = input(
                    "Categoría: "
                ).strip()

                precio = float(
                    input("Precio: ")
                )

                stock = int(
                    input("Stock: ")
                )

                producto = Producto(
                    codigo,
                    nombre,
                    categoria,
                    precio,
                    stock
                )

                if restaurante.registrar_producto(
                    producto
                ):

                    ArchivoServicio.guardar_productos(
                        RUTA_PRODUCTOS,
                        restaurante.listar_productos()
                    )

                    print(
                        "Producto registrado correctamente."
                    )

                else:

                    print(
                        "Ya existe un producto "
                        "con ese código."
                    )

            except ValueError as error:

                print(f"Error: {error}")

        # ==================================
        # 2. BUSCAR PRODUCTO
        # ==================================

        elif opcion == "2":

            codigo = input(
                "Ingrese el código del producto: "
            ).strip()

            producto = restaurante.buscar_producto(
                codigo
            )

            if producto is not None:

                print("\nProducto encontrado:")
                print(producto)

            else:

                print(
                    "Producto no encontrado."
                )

        # ==================================
        # 3. ACTUALIZAR PRODUCTO
        # ==================================

        elif opcion == "3":

            try:

                codigo = input(
                    "Código del producto: "
                ).strip()

                nombre = input(
                    "Nuevo nombre: "
                ).strip()

                categoria = input(
                    "Nueva categoría: "
                ).strip()

                precio = float(
                    input("Nuevo precio: ")
                )

                stock = int(
                    input("Nuevo stock: ")
                )

                actualizado = (
                    restaurante.actualizar_producto(
                        codigo,
                        nombre,
                        categoria,
                        precio,
                        stock
                    )
                )

                if actualizado:

                    ArchivoServicio.guardar_productos(
                        RUTA_PRODUCTOS,
                        restaurante.listar_productos()
                    )

                    print(
                        "Producto actualizado correctamente."
                    )

                else:

                    print(
                        "Producto no encontrado."
                    )

            except ValueError as error:

                print(f"Error: {error}")

        # ==================================
        # 4. ELIMINAR PRODUCTO
        # ==================================

        elif opcion == "4":

            codigo = input(
                "Código del producto: "
            ).strip()

            eliminado = restaurante.eliminar_producto(
                codigo
            )

            if eliminado:

                ArchivoServicio.guardar_productos(
                    RUTA_PRODUCTOS,
                    restaurante.listar_productos()
                )

                print(
                    "Producto eliminado correctamente."
                )

            else:

                print(
                    "Producto no encontrado."
                )

        # ==================================
        # 5. LISTAR PRODUCTOS
        # ==================================

        elif opcion == "5":

            productos_actuales = (
                restaurante.listar_productos()
            )

            if not productos_actuales:

                print(
                    "No existen productos registrados."
                )

            else:

                print("\n========== PRODUCTOS ==========")

                for producto in productos_actuales:

                    print(producto)

        # ==================================
        # 6. REGISTRAR USUARIO
        # ==================================

        elif opcion == "6":

            try:

                identificacion = input(
                    "Identificación: "
                ).strip()

                nombre = input(
                    "Nombre: "
                ).strip()

                usuario = Usuario(
                    identificacion,
                    nombre
                )

                if restaurante.registrar_usuario(
                    usuario
                ):

                    ArchivoServicio.guardar_usuarios(
                        RUTA_USUARIOS,
                        restaurante.listar_usuarios()
                    )

                    print(
                        "Usuario registrado correctamente."
                    )

                else:

                    print(
                        "Ya existe un usuario "
                        "con esa identificación."
                    )

            except ValueError as error:

                print(f"Error: {error}")

        # ==================================
        # 7. LISTAR USUARIOS
        # ==================================

        elif opcion == "7":

            usuarios_actuales = (
                restaurante.listar_usuarios()
            )

            if not usuarios_actuales:

                print(
                    "No existen usuarios registrados."
                )

            else:

                print("\n========== USUARIOS ==========")

                for usuario in usuarios_actuales:

                    print(usuario)

        # ==================================
        # 8. CATEGORÍAS
        # ==================================

        elif opcion == "8":

            categorias = (
                restaurante.obtener_categorias()
            )

            if not categorias:

                print(
                    "No existen categorías."
                )

            else:

                print(
                    "\n========== CATEGORÍAS =========="
                )

                for categoria in sorted(categorias):

                    print(
                        f"- {categoria}"
                    )

        # ==================================
        # 9. REALIZAR VENTA
        # ==================================

        elif opcion == "9":

            try:

                identificacion = input(
                    "Identificación del usuario: "
                ).strip()

                codigo = input(
                    "Código del producto: "
                ).strip()

                cantidad = int(
                    input("Cantidad a comprar: ")
                )

                resultado = (
                    restaurante.vender_producto(
                        codigo,
                        identificacion,
                        cantidad
                    )
                )

                if resultado:

                    ArchivoServicio.guardar_productos(
                        RUTA_PRODUCTOS,
                        restaurante.listar_productos()
                    )

                    ArchivoServicio.guardar_ventas(
                        RUTA_VENTAS,
                        restaurante.listar_ventas()
                    )

                    print(
                        "Venta registrada correctamente."
                    )

                    producto = restaurante.buscar_producto(
                        codigo
                    )

                    if producto is not None:

                        print(
                            f"Stock disponible: "
                            f"{producto.stock}"
                        )

                else:

                    print(
                        "No se pudo realizar la venta."
                    )

                    print(
                        "Verifique que el usuario, "
                        "producto, cantidad y stock "
                        "sean correctos."
                    )

            except ValueError:

                print(
                    "Error: la cantidad debe ser "
                    "un número entero."
                )

        # ==================================
        # 10. CONSULTAR VENTAS POR USUARIO
        # ==================================

        elif opcion == "10":

            identificacion = input(
                "Identificación del usuario: "
            ).strip()

            usuario = restaurante.buscar_usuario(
                identificacion
            )

            if usuario is None:

                print(
                    "Usuario no encontrado."
                )

                continue

            ventas_usuario = (
                restaurante.consultar_ventas_usuario(
                    identificacion
                )
            )

            if not ventas_usuario:

                print(
                    "El usuario no tiene "
                    "ventas registradas."
                )

            else:

                print(
                    f"\nVentas del usuario: "
                    f"{usuario.nombre}"
                )

                print(
                    "================================"
                )

                for venta in ventas_usuario:

                    producto = (
                        restaurante.buscar_producto(
                            venta.producto_codigo
                        )
                    )

                    if producto is not None:

                        print(
                            f"Producto: {producto.nombre}"
                        )

                        print(
                            f"Código: {producto.codigo}"
                        )

                        print(
                            f"Cantidad: {venta.cantidad}"
                        )

                        print(
                            "--------------------------------"
                        )

                    else:

                        print(
                            f"Producto: "
                            f"{venta.producto_codigo}"
                        )

                        print(
                            f"Cantidad: "
                            f"{venta.cantidad}"
                        )

        # ==================================
        # 11. LISTAR VENTAS
        # ==================================

        elif opcion == "11":

            ventas_actuales = (
                restaurante.listar_ventas()
            )

            if not ventas_actuales:

                print(
                    "No existen ventas registradas."
                )

            else:

                print(
                    "\n========== VENTAS =========="
                )

                for venta in ventas_actuales:

                    print(venta)

        # ==================================
        # 12. SALIR
        # ==================================

        elif opcion == "12":

            print(
                "Programa finalizado."
            )

            break

        else:

            print(
                "Opción inválida."
            )


if __name__ == "__main__":
    main()