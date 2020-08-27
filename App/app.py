"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

# C:\\Users\\home\\Desktop\\LABORATORIOS\\Lab2_202020\\Data\\MoviesCastingRaw-small.csv
# C:\\Users\\home\\Desktop\\LABORATORIOS\\Lab2_202020\\Data\\SmallMoviesDetailsCleaned.csv




from time import process_time
import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import mergesort as me
def loadCSVFile(movies, casting, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    st = lt.newList("ARRAY_LIST")  # Usando implementacion arraylist
    # lst = lt.newList()  # Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time()  # tiempo inicial
    dialect = csv.excel()
    dialect.delimiter = sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                lt.addLast(lst, row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop-t1_start, " segundos")
    return st


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar Rankings de películas")
    print("6- Consultar un director en particular")
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size'] == 0:
        print("La lista esta vacía")
        return 0
    else:
        t1_start = process_time()  # tiempo inicial
        counter = 0
        iterator = it.newIterator(lst)
        while it.hasNext(iterator):
            element = it.next(iterator)
            # filtrar por palabra clave
            if criteria.lower() in element[column].lower():
                counter += 1
        t1_stop = process_time()  # tiempo final
        print("Tiempo de ejecución ", t1_stop-t1_start, " segundos")
    return counter


def countElementsByCriteria(criteria, lst_casting, lst_movies):

    # Requirimiento 3
    t1_start = process_time()  # tiempo inicial

    list_id = lt.new("ARRAY_LIST")
    peliculas = 0
    for posicion in range(lt.size(lst_casting)):
        name_director = lt.getElement(lst_casting, posicion)
        if name_director["director_name"].lower() == criteria.lower():
            ides = lt.addFirst(list_id, name_director["id"])
            peliculas += 1

    list_movies_name = lt.new("ARRAY_LIST")
    promedio_vote_average = lt.new("ARRAY_LIST")
    for idenficador in list_id:
        movies = lt.getElement(lst_movies, idenficador)
        lt.addFirst(list_movies_name, movies["original_title"])
        lt.addFirst(promedio_vote_average, float(movies["vote_average"]))

    longitud = list_vote_average
    suma_promedio = 0
    for suma in promedio_vote_average:
        suma_promedio += suma
    t2_stop = process_time()  # tiempo final
    print("Tiempo de ejecución ", t1_stop-t1_start, " segundos")
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    return (list_movies_name, longitud, suma_promedio / longitud)


def orderElementsByCriteria(ingreso_dato, criteria, sentido, lst_movies):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """

    return 0


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista_casting = lt.newList("ARRAY_LIST")  # se require usar lista definida
    lista_movies = lt.newList("ARRAY_LIST")  # se require usar lista definida
    while True:
        printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input('Seleccione una opción para continuar\n')
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                # llamar funcion cargar datos
                lista = loadCSVFile(
                    "C:\\Users\\home\\Desktop\\LABORATORIOS\\Lab2_202020\\Data\\MoviesCastingRaw-small.csv")
                print("Datos cargados, ",
                      lista['size'], " elementos cargados")
                print("Datos cargados, ",
                      lista['size'], " elementos cargados")

            elif int(inputs[0]) == 2:  # opcion 2
                # obtener la longitud de la lista
                if lista == None or lista['size'] == 0:
                    print("La lista esta vacía")
                else:
                    print("La lista tiene ",
                          lista_casting['size'], " elementos")
                    print("La lista tiene ",
                          lista_movies['size'], " elementos")

            elif int(inputs[0]) == 3:  # opcion 3
                # obtener la longitud de la lista
                if lista == None or lista['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    counter = countElementsFilteredByColumn(
                        criteria, "nombre", lista)  # filtrar una columna por criterio
                    counter = countElementsFilteredByColumn(
                        criteria, "nombre", lista)
                    print("Coinciden ", counter,
                          " elementos con el crtierio: ", criteria)

            elif int(inputs[0]) == 4:  # opcion 4
                # obtener la longitud de la lista
                if lista == None or lista['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    counter = countElementsByCriteria(criteria, 0, lista)
                    print("Coinciden ", counter, " elementos con el crtierio: '",
                          criteria, "' (en construcción ...)")

            elif int(inputs[0]) == 5:  # opcion 5
                # obtener la longitud de la lista
                if lista == None or lista['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    counter = countElementsFilteredByColumn(
                        criteria, lista_casting, lista_movies)  # filtrar una columna por criterio
                    print("Coinciden ", counter, " elementos con el crtierio: '",
                          criteria, "' (en construcción ...)")

            elif int(inputs[0]) == 6:  # opcion 6
                # obtener la longitud de la lista
                if lista == None or lista['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = int(input('Ingrese el criterio de búsqueda\n'))
                    counter = orderElementsByCriteria(
                        function, criteria, lista_movies)
                    print("Coinciden ", counter, " elementos con el crtierio: '",
                          criteria, "' (en construcción ...)")

            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
