"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

from ctypes import resize
from itertools import count
from os import system
import random

if system("clear") != 0:
    system("cls")


# def cantidad_de_letras():
#     n = input("Escriba el nombre que desea: ").upper()
#     r = input("Escriba la letra de desea contar: ").upper()

#     r = n.count(r)
#     print(r)


# cantidad_de_letras()


# def cantidad_de_letras():
#     reed = "Reed Richards".upper()

#     r = reed.count("r".upper())

#     print(r)

#     jhon = "Johnny Storm".upper()

#     j = jhon.count("j".upper())

#     print(j)

#     if r == j:
#         r = True
#         print(f"La cantidad de letras son iguales: {r}")

#     elif not r == j:

#         r = False
#         print(f"La cantidad de letras son diferentes: {r}")

#     else:
#         return True


# cantidad_de_letras()
text = "rrrrjRjjjJ"


def cantidad_de_letras(text):
    text = text.upper()
    count_r = text.count("R")
    count_j = text.count("J")
    print(f"count_r: {count_r} count_j: {count_j}")

    # if count_r == count_j:
    #     return True
    # else:
    #     return False

    return count_r == count_j


cantidad_de_letras("RrrrrJJJJJjjdddj")
cantidad_de_letras("RrrJjj")

from os import system

if system("clear") != 0:
    system("cls")

# def find_first_sum(nums, goal):
#   # early return, una validación rápida
#   if len(nums) == 0: return None

#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       if nums[i] + nums[j] == goal:
#         return [i, j]

#   return None # no se encontró ninguna combinación


# def find_first_sum(nums, goal):
#     seen = {}  # diccionario para guardar el numero y su índice

#     for index, value in enumerate(nums):
#         missing = goal - value
#         if missing in seen:
#             return [seen[missing], index]
#         seen[value] = (
#             index  # guardar el número actual a los vistos, porque no hemos encontrado la combinación
#         )

#     return None


# nums = [4, 5, 6, 2]
# goal = 8
# result = find_first_sum(nums, goal)  # [2, 3]
# print(result)


"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""


def find_first_sum(nums, goal):
    # early return, una validación rápida
    if len(nums) == 0:
        return None

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]

    return None  # no se encontró ninguna combinación


nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal)  # [2, 3]
print(result)
