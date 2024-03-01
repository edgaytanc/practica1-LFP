from clases.pelicula import Pelicula
from clases.gestorPelicula import GestorPelicula
from clases.desarollador import Desarrollador

gestor = GestorPelicula()
desarrollador = Desarrollador("Lenguajes Formales y de Programacion",'P',"9712749","Edgar David Gaytan Carranza")

def cargar_archivo():
    print("\nArchivo Cargado con exito...")
    print()

    # Ruta al archivo con los datos de las peliculas
    ruta_archivo = 'peliculas.flp'

    # Cargar las peliculas utilizando el metodo cargar_archivo
    
    gestor.cargar_archivo(ruta_archivo)

    # imprime los detalles de cada pelicula cargada
    # gestor.mostrar_peliculas()

def gestionar_peliculas():
    
    gestor.mostrar_menu_gestion_peliculas()

def filtrar_informacion():
    gestor.mostrar_menu_filtrado()

def viaualizar_datos():
    gestor.generar_grafica()

def mostar_menu_principal():
    while True:
        print(f"{'-'*10} Menu principal {'-'*10}")
        print("1. Cargar archivo")
        print("2. Gestionar peliculas")
        print("3. Filtrar informacion")
        print("4. Visualizar datos")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            cargar_archivo()
        elif opcion == '2':
            gestionar_peliculas()
        elif opcion == '3':
            filtrar_informacion()
        elif opcion == '4':
            viaualizar_datos()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo")

if __name__ == "__main__":
    desarrollador.desplegar_datos_desarrollador()
    mostar_menu_principal()