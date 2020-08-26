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


# from Sorting import insertionsort as sort
# from Sorting import shellsort as sort
# from Sorting import mselectionsort as sortS




import config as cf
import sys
import csv
from Sorting import mergesort as sort
from DataStructures import liststructure as lt
from DataStructures import listiterator as it
from time import process_time
from ADT import list as lt
def loadCSVFile(file, sep=";"):
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
    lst = lt.newList("ARRAY_LIST")  # Usando implementacion arraylist
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
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Crear Ranking de películas")
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

# Req 3 del reto


def countElementsByCriteria(criteria, lstCast, lstMov):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    idMov = lt.newList("ARRAY_LIST")

    for i in range(lt.size(lstCast)):
        director = lt.getElement(lstCast, i)
        if criteria == director['director_name']:
            lt.addLast(idMov, i)

    pelicula = lt.newList("ARRAY_LIST")
    numPel = 0
    calProm = 0.0

    for i in range(lt.size(idMov)):
        pos = lt.getElement(idMov, i)
        lt.addLast(pelicula, lt.getElement(lstMov, pos)['original_title'])
        numPel += 1
        calProm += float(lt.getElement(lstMov, i)['vote_average'])

    return pelicula, numPel, calProm/numPel

# Req 2 del reto


def orderElementsByCriteria(x, criteria, sentido, lst):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if criteria == 0 and sentido == 0:
        sort.mergesort(lst, lessV)
    elif criteria == 0 and sentido == 1:
        sort.mergesort(lst, greaterV)
    elif criteria == 1 and sentido == 0:
        sort.mergesort(lst, lessA)
    else:
        sort.mergesort(lst, greaterA)

    return lt.subList(lst, 1, x)


def lessV(element1, element2):
    if float(element1['vote_count']) < float(element2['vote_count']):
        return True
    return False


def greaterV(element1, element2):
    if float(element1['vote_count']) > float(element2['vote_count']):
        return True
    return False


def lessA(element1, element2):
    if float(element1['vote_average']) < float(element2['vote_average']):
        return True
    return False


def greaterA(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None
    """
    listaCasting = lt.newList("ARRAY_LIST")  # se require usar lista definida
    listaMovies = lt.newList("ARRAY_LIST")  # se require usar lista definida

    while True:
        printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input('Seleccione una opción para continuar\n')
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                # llamar funcion cargar datos
                listaCasting = loadCSVFile(
                    cf.data_dir + 'MoviesCastingRaw-small.csv')

                listaMovies = loadCSVFile(
                    cf.data_dir + 'SmallMoviesDetailsCleaned.csv')

                print("Datos Casting cargados, ",
                      listaCasting['size'], " elementos cargados")

                print("Datos Movies cargados, ",
                      listaMovies['size'], " elementos cargados")
            elif int(inputs[0]) == 2:  # opcion 2
                # obtener la longitud de la lista
                if listaCasting == None or listaCasting['size'] == 0:
                    print("La lista esta vacía")
                else:
                    print("La lista tiene ",
                          listaCasting['size'], " elementos")
            elif int(inputs[0]) == 3:  # opcion 3
                # obtener la longitud de la lista
                if listaCasting == None or listaCasting['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    counter = countElementsFilteredByColumn(
                        criteria, "nombre", listaCasting)  # filtrar una columna por criterio
                    print("Coinciden ", counter,
                          " elementos con el crtierio: ", criteria)
            elif int(inputs[0]) == 4:  # opcion 4
                # obtener la longitud de la lista
                if listaCasting == None or listaCasting['size'] == 0:
                    print("La lista esta vacía")
                else:
                    criteria = input('Ingrese el criterio de búsqueda\n')
                    mov, numPel, prom = countElementsByCriteria(
                        criteria, listaCasting, listaMovies)
                    print("Coinciden ", numPel, " elementos con el crtierio: '",
                          criteria, "' com una calificación promedio de '", prom, "' peliculas:", mov)
            elif int(inputs[0]) == 5:  # opcion 5
                # obtener la longitud de la lista
                if listaMovies == None or listaMovies['size'] == 0:
                    print("La lista esta vacía")
                else:
                    x = int(input(
                        'Ingrese la cantidad de elementos que desea\n'))
                    if x < 10:
                        print("Debe ser mayor a 10")
                    else:
                        criteria = int(input(
                            'Ingrese 0 para ordenar por número de votos o 1 para ordenar por votación promedio\n')[0])

                        if criteria != 0 and criteria != 1:
                            print("La opción ingresa no es valida")
                        else:
                            sentido = int(input(
                                'Ingrese 0 para hacer orden ascendente o 1 para descendente\n')[0])

                            if sentido != 0 and sentido != 1:
                                print("La opción ingresa no es valida")
                            else:
                                topOrder = orderElementsByCriteria(
                                    x, criteria, sentido, listaMovies
                                )
                                print(
                                    "Top ", x, topOrder)
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
