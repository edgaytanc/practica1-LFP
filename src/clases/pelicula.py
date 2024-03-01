class Pelicula:
    def __init__(self, nombre, actores, anio, genero):
        self.nombre = nombre
        self.actores = actores
        self.anio = anio
        self.genero = genero

    def __str__(self):
        return f"{self.nombre} - {self.anio} - {self.genero} - Actores: {', '.join(self.actores)}"