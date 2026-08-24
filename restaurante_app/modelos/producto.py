class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ):
        if not codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")

        if precio < 0:
            raise ValueError("El precio del producto no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }