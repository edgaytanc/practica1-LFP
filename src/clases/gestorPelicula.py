from .pelicula import Pelicula
from graphviz import Digraph

class GestorPelicula:
    def __init__(self):
        self.peliculas = []

    def cargar_archivo(self,ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                nombre, actores_str, anio, genero = linea.strip().split(';')
                actores = actores_str.split(',')
                
                # Verifica si la pelicula ya existe
                existente = next((p for p in self.peliculas if p.nombre ==nombre), None)
                if existente:
                    # Si la pelicula ya existe, la elimina
                    self.peliculas.remove(existente)
                # Agrega la nueva instancia de Pelicula
                self.peliculas.append(Pelicula(nombre,actores,int(anio), genero.strip()))
    
    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print(pelicula)

    def listado_peliculas(self):
        # Encabezado de la tabla
        print(f"{'Indice':<8}{'Nombre':<30}{'Año':<6}{'Genero':<15}{'Actores'}")
        print('_'*80)

        for indice, pelicula in enumerate(self.peliculas, start=1):
            # Unir los actorescon comas y limitar la longitud para evitar desbordamiento
            actores = ', '.join(pelicula.actores)
            if len(actores) > 50: # Limitar la longitud de la cadena de actores para mejora la presntacion
                actores = actores[:47] + '...'
            # Imprimir cadena pelicula en una nueva fila de la tabla
            print(f"{indice:<8}{pelicula.nombre:<30}{pelicula.anio:<6}{pelicula.genero:<15}{actores}")


    # Funciones para manejo de gestion de pelicualas
    def muestra_peliculas(self):
        for indice, pelicula in enumerate(self.peliculas, start=1):
            print(f"{indice}. {pelicula.nombre}")

    def mostrar_actores_pelicula(self):
        self.muestra_peliculas()
        seleccion = input("Seleccione el número de la película para ver sus actores: ")
        try:
            indice_pelicula = int(seleccion) - 1  # Ajustar a índice basado en 0
            pelicula_seleccionada = self.peliculas[indice_pelicula]
            print(f"\nActores de '{pelicula_seleccionada.nombre}':")
            print("-" * 50)  # Línea para separar visualmente el título de la lista de actores
            for actor in pelicula_seleccionada.actores:
                print(f" - {actor}")
        except (ValueError, IndexError):
            print("Selección no válida. Por favor, introduzca un número de lista válido.")

    def mostrar_menu_gestion_peliculas(self):
        while True:
            print("\n Gention de Peliculas")
            print("a. Mostrar peliculas")
            print("b. Mostar actores de una pelicula")
            print("c. Volver")

            opcion = input("Seleccione una opcion: ").lower()

            if opcion == 'a':
                self.listado_peliculas()
            elif opcion == 'b':
                self.mostrar_actores_pelicula()
            elif opcion == 'c':
                break
            else:
                print("Opcion no valida, por favor intent de nuevo.")


    # flitros varios
            
    def filtrar_por_actor(self, actor_nombre):
        peliculas_actor = [pelicula for pelicula in self.peliculas if actor_nombre in pelicula.actores]
        if peliculas_actor:
            for pelicula in peliculas_actor:
                print(f"{pelicula.nombre} - {pelicula.genero}")
        else:
            print(f"No se encontraron peliculas con el actor: {actor_nombre}")
    
    def filtrar_por_anio(self, anio):
        peliculas_anio = [pelicula for pelicula in self.peliculas if pelicula.anio == anio]
        if peliculas_anio:
            for pelicula in peliculas_anio:
                print(f"{pelicula.nombre} - {pelicula.genero}")
        else:
            print(f"No se encontraron películas del año: {anio}")

    def filtrar_por_genero(self, genero):
        peliculas_genero = [pelicula for pelicula in self.peliculas if pelicula.genero.lower() == genero.lower()]
        if peliculas_genero:
            for pelicula in peliculas_genero:
                print(f"{pelicula.nombre} - {pelicula.anio}")
        else:
            print(f"No se encontraron películas del género: {genero}")

    def mostrar_menu_filtrado(self):
        while True:
            print("\nMenú de Filtrado")
            print("a. Filtrado por actor")
            print("b. Filtrado por año")
            print("c. Filtrado por género")
            print("d. Volver")

            opcion = input("seleccione una opcion: ").lower()

            if opcion == 'a':
                actor = input("Ingrese el nombre del actor: ")
                self.filtrar_por_actor(actor)
            elif opcion == 'b':
                try:
                    anio = int(input("Ingrese el año: "))
                    self.filtrar_por_anio(anio)
                except ValueError:
                    print("Por favor, ingrese un año válido.")
            elif opcion == 'c':
                genero = input("Ingrese el género: ")
                self.filtrar_por_genero(genero)
            elif opcion == 'd':
                break
            else:
                print("Opcion no valida, por favor intente de nuevo.")

    
    def generar_grafica(self):
        # Crea un objeto diagrahp para la visualizacion
        dot = Digraph(comment='Peliculas', graph_attr={'rankdir': 'LR'})

        # Agregar nodo y aristas al grafico
        for pelicula in self.peliculas:
            # Crea un identificador unico para cada pelicula basado en su nombre y anione
            pelicula_id = f"{pelicula.nombre.replace(' ', '_')}_{pelicula.anio}"
            # Agrega nodo de pelicula al grafico
            dot.node(pelicula_id, f"{pelicula.nombre}\n{pelicula.anio}\n{pelicula.genero}", shape='box', color='blue', style='filled', fillcolor='lightblue2')

            # Agregar nodos de actores y aristas entre peliculas y actores
            for actor in pelicula.actores:
                actor_id = actor.replace(' ','_')
                dot.node(actor_id, actor, shape='box', color='green', style='filled', fillcolor='palegreen')
                dot.edge(pelicula_id, actor_id)

        # Renderizar y visualizar el grafico
        dot.render('peliculas_graph', view=True)
