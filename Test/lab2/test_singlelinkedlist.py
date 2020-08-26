# Testear usando el archivo de peliculas y elencos
import pytest
import config as cf
import csv
from DataStructures import singlelinkedlist as alt

# Es la función de comparación ue va a usar nuestra lista


def cmpfunction(element1, element2):
    if element1 == element2:
        return 0

# Generamos una lista vacia y le pasamos como parametros la función de comparación


@pytest.fixture
def lstCasting():
    lstCasting = alt.newList(cmpfunction)
    return lstCasting


@pytest.fixture
def lstMovies():
    lstMovies = alt.newList(cmpfunction)
    return lstMovies

# Creamos una arrego con los elementos que leímos y luego usaremos


@pytest.fixture
def casting():
    casting = []
    file = cf.data_dir + 'MoviesCastingRaw-small.csv'
    dialect = csv.excel()
    dialect.delimiter = ";"
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            casting.append(row)

    return casting


@pytest.fixture
def movies():
    movies = []
    file = cf.data_dir + 'SmallMoviesDetailsCleaned.csv'
    dialect = csv.excel()
    dialect.delimiter = ";"
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            movies.append(row)
    return movies


# Creamos una lista que contiene todos los elementos quel leimos


@pytest.fixture
def lstCasting2(casting):
    lstCasting2 = alt.newList(cmpfunction)
    for i in range(0, len(casting)):
        alt.addLast(lstCasting2, casting[i])
    return lstCasting2


@pytest.fixture
def lstMovies2(movies):
    lstMovies2 = alt.newList(cmpfunction)
    for i in range(0, len(movies)):
        alt.addLast(lstMovies2, movies[i])
    return lstMovies2


def test_isEmpty(lstCasting, lstMovies):
    assert alt.isEmpty(lstCasting) == True
    assert alt.size(lstCasting) == 0

    assert alt.isEmpty(lstMovies) == True
    assert alt.size(lstMovies) == 0


def test_addFirst(lstCasting, lstMovies, casting, movies):
    assert alt.isEmpty(lstCasting) == True
    assert alt.size(lstCasting) == 0
    alt.addFirst(lstCasting, casting[0])
    assert alt.size(lstCasting) == 1
    alt.addFirst(lstCasting, casting[5])
    assert alt.size(lstCasting) == 2

    assert alt.isEmpty(lstMovies) == True
    assert alt.size(lstMovies) == 0
    alt.addFirst(lstMovies, movies[0])
    assert alt.size(lstMovies) == 1
    alt.addFirst(lstMovies, movies[5])
    assert alt.size(lstMovies) == 2


def test_addLast(lstCasting, lstMovies, casting, movies):
    assert alt.isEmpty(lstCasting) == True
    assert alt.size(lstCasting) == 0
    alt.addLast(lstCasting, casting[0])
    assert alt.size(lstCasting) == 1
    alt.addLast(lstCasting, casting[5])
    assert alt.size(lstCasting) == 2

    assert alt.isEmpty(lstMovies) == True
    assert alt.size(lstMovies) == 0
    alt.addLast(lstMovies, movies[0])
    assert alt.size(lstMovies) == 1
    alt.addLast(lstMovies, movies[5])
    assert alt.size(lstMovies) == 2


def test_getElement(lstCasting2, lstMovies2, casting, movies):
    casting2 = alt.getElement(lstCasting2, 1)
    assert casting2 == casting[0]
    casting2 = alt.getElement(lstCasting2, 5)
    assert casting2 == casting[4]

    movie2 = alt.getElement(lstMovies2, 1)
    assert movie2 == movies[0]
    movie2 = alt.getElement(lstMovies2, 5)
    assert movie2 == movies[4]


def test_removeFirst(lstCasting2, lstMovies2, casting, movies):
    assert alt.size(lstCasting2) == len(casting)
    alt.removeFirst(lstCasting2)
    assert alt.size(lstCasting2) == len(casting)-1
    casting2 = alt.getElement(lstCasting2, 1)
    assert casting2 == casting[1]

    assert alt.size(lstMovies2) == len(movies)
    alt.removeFirst(lstMovies2)
    assert alt.size(lstMovies2) == len(movies)-1
    movies2 = alt.getElement(lstMovies2, 1)
    assert movies2 == movies[1]


def test_removeLast(lstCasting2, lstMovies2, casting, movies):
    assert alt.size(lstCasting2) == len(casting)
    alt.removeLast(lstCasting2)
    assert alt.size(lstCasting2) == len(casting)-1
    casting2 = alt.getElement(lstCasting2, alt.size(lstCasting2))
    assert casting2 == casting[len(casting)-2]

    assert alt.size(lstMovies2) == len(movies)
    alt.removeLast(lstMovies2)
    assert alt.size(lstMovies2) == len(movies)-1
    movies2 = alt.getElement(lstMovies2, alt.size(lstMovies2))
    assert movies2 == movies[len(movies)-2]


def test_insertElement(lstCasting, lstMovies, casting, movies):
    assert alt.isEmpty(lstCasting) is True
    assert alt.size(lstCasting) == 0
    alt.insertElement(lstCasting, casting[0], 1)
    assert alt.size(lstCasting) == 1
    alt.insertElement(lstCasting, casting[1], 2)
    assert alt.size(lstCasting) == 2
    alt.insertElement(lstCasting, casting[2], 1)
    assert alt.size(lstCasting) == 3
    cast = alt.getElement(lstCasting, 1)
    assert cast == casting[2]
    cast = alt.getElement(lstCasting, 2)
    assert cast == casting[0]

    assert alt.isEmpty(lstMovies) is True
    assert alt.size(lstMovies) == 0
    alt.insertElement(lstMovies, movies[0], 1)
    assert alt.size(lstMovies) == 1
    alt.insertElement(lstMovies, movies[1], 2)
    assert alt.size(lstMovies) == 2
    alt.insertElement(lstMovies, movies[2], 1)
    assert alt.size(lstMovies) == 3
    mov = alt.getElement(lstMovies, 1)
    assert mov == movies[2]
    mov = alt.getElement(lstMovies, 2)
    assert mov == movies[0]


def test_deleteElement(lstCasting2, lstMovies2, casting, movies):
    pos = alt.isPresent(lstCasting2, casting[2])
    assert pos > 0
    cast = alt.getElement(lstCasting2, pos)
    assert cast == casting[2]
    alt.deleteElement(lstCasting2, pos)
    assert alt.size(lstCasting2) == len(casting)-1
    cast = alt.getElement(lstCasting2, pos)
    assert cast == casting[3]

    pos = alt.isPresent(lstMovies2, movies[2])
    assert pos > 0
    movie = alt.getElement(lstMovies2, pos)
    assert movie == movies[2]
    alt.deleteElement(lstMovies2, pos)
    assert alt.size(lstMovies2) == len(movies)-1
    movie = alt.getElement(lstMovies2, pos)
    assert movie == movies[3]


def test_changeInfo(lstCasting2, lstMovies2):
    castY = alt.getElement(lstCasting2, 1)
    castY['id'] = alt.size(lstCasting2)+1
    alt.changeInfo(lstCasting2, 1, castY)
    cast = alt.getElement(lstCasting2, 1)
    assert castY == cast

    movY = alt.getElement(lstMovies2, 1)
    movY['id'] = alt.size(lstMovies2)+1
    alt.changeInfo(lstMovies2, 1, movY)
    mov = alt.getElement(lstMovies2, 1)
    assert movY == mov


def test_isPresent(lstCasting2, lstMovies2, casting, movies):
    cast = {'id': len(casting)*2}
    assert alt.isPresent(lstCasting2, casting[1]) > 0
    assert alt.isPresent(lstCasting2, cast) == 0

    movie = {'id': len(movies)*2}
    assert alt.isPresent(lstMovies2, movies[1]) > 0
    assert alt.isPresent(lstMovies2, movie) == 0


def test_exchange(lstCasting2, lstMovies2):
    casting1 = alt.getElement(lstCasting2, 1)
    casting5 = alt.getElement(lstCasting2, 5)
    alt.exchange(lstCasting2, 1, 5)
    assert alt.getElement(lstCasting2, 1) == casting5
    assert alt.getElement(lstCasting2, 5) == casting1

    movie1 = alt.getElement(lstMovies2, 1)
    movie5 = alt.getElement(lstMovies2, 5)
    alt.exchange(lstMovies2, 1, 5)
    assert alt.getElement(lstMovies2, 1) == movie5
    assert alt.getElement(lstMovies2, 5) == movie1
