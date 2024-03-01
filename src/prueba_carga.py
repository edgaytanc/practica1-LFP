# importaciones
from clases.pelicula import Pelicula
from clases.gestorPelicula import GestorPelicula

# Ruta al archivo con los datos de las peliculas
ruta_archivo = 'peliculas.flp'

# Cargar las peliculas utilizando el metodo cargar_archivo
gestor = GestorPelicula()
gestor.cargar_archivo(ruta_archivo)

# imprime los detalles de cada pelicula cargada
gestor.mostrar_peliculas()
peliculas = gestor.peliculas

gestor.mostrar_actores_pelicula(peliculas)