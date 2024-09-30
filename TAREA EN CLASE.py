
class Libro:
    def __init__(self, nombre, categoria, num_hojas, autor):
        self.nombre = nombre
        self.categoria = categoria
        self.num_hojas = num_hojas
        self.autor = autor

    def imprimir_info(self):
        print("Información del Libro:")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Número de hojas: {self.num_hojas}")
        print(f"Autor: {self.autor}")


# Crear un objeto Libro
libro1 = Libro(
    nombre="EL PATITO FEO",
    categoria="CUENTO",
    num_hojas=50,
    autor="KEVIN M,N"
)


# Imprimir la información del libro
libro1.imprimir_info()