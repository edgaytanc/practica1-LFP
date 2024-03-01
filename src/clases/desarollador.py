class Desarrollador:
    def __init__(self,curso, seccion, carne, nombre):
        self.curso = curso
        self.seccion = seccion
        self.carne = carne
        self.nombre = nombre

    def desplegar_datos_desarrollador(self):
        print(f"{self.curso}".upper())
        print(f"Seccion: {self.seccion}")
        print(f"Carne: {self.carne}")
        print(f"Nombre: {self.nombre}")

        tecla = input()