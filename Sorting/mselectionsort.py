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

import config as cf
from ADT import list as lt


def selectionSort(lst, lessfunction, criteria):
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1              # minimun tiene el menor elemento conocido hasta ese momento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (lessfunction(lt.getElement(lst, pos2), lt.getElement(lst, minimum), criteria)):
                minimum = pos2      # minimum se actualiza con la posición del nuevo elemento más pequeño
            pos2 += 1
        # se intercambia el elemento más pequeño hasta ese punto con el elemento en pos1
        lt.exchange(lst, pos1, minimum)
        pos1 += 1