"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 *
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


import pytest
import config as cf
from Sorting import minsertionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv


# Creamos una arrego con los elementos que leímos y luego usaremos
@pytest.fixture
def movies():
    list_type = 'ARRAY_LIST'
    #list_type = 'SINGLE_LINKED'
    movies = lt.newList(list_type)

    file = cf.data_dir + 'SmallMoviesDetailsCleaned.csv'
    dialect = csv.excel()
    dialect.delimiter = ";"
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            lt.addLast(movies, row)

    return movies


def less(element1, element2, criteria):
    if float(element1[criteria]) < float(element2[criteria]):
        return True
    return False


def greater(element1, element2, criteria):
    if float(element1[criteria]) > float(element2[criteria]):
        return True
    return False


def test_sortlesscount(movies):
    """
    Lista con elementos en ordenador por id
    """
    print("sorting ....")
    count = 'vote_count'
    sort.insertionSort(movies, less, count)
    while not (lt.isEmpty(movies)):
        x = float(lt.removeLast(movies)[count])
        if not (lt.isEmpty(movies)):
            y = float(lt.lastElement(movies)[count])
        else:
            break
        assert x >= y


def test_sortlessaverage(movies):
    """
    Lista con elementos en ordenador por id
    """
    print("sorting ....")
    criteria = 'vote_average'
    sort.insertionSort(movies, less, criteria)
    while not (lt.isEmpty(movies)):
        x = float(lt.removeLast(movies)[criteria])
        if not (lt.isEmpty(movies)):
            y = float(lt.lastElement(movies)[criteria])
        else:
            break
        assert x >= y


def test_sortgreatercount(movies):
    """
    Lista con elementos en ordenador por id
    """
    print("sorting ....")
    count = 'vote_count'
    sort.insertionSort(movies, greater, count)
    while not (lt.isEmpty(movies)):
        x = float(lt.removeLast(movies)[count])
        if not (lt.isEmpty(movies)):
            y = float(lt.lastElement(movies)[count])
        else:
            break
        assert x <= y


def test_sortgreateraverage(movies):
    """
    Lista con elementos en ordenador por id
    """
    print("sorting ....")
    criteria = 'vote_average'
    sort.insertionSort(movies, greater, criteria)
    while not (lt.isEmpty(movies)):
        x = float(lt.removeLast(movies)[criteria])
        if not (lt.isEmpty(movies)):
            y = float(lt.lastElement(movies)[criteria])
        else:
            break
        assert x <= y
