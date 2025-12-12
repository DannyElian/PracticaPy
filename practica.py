from statistics import median


print("Este es mi primer programa en Python")
print("--------------------------------")

""" Primer ejercicio en python """
"""
nombre = "Danny Elian"
Apellido = "Medina Cuello"

nombre_completo = nombre + " " + Apellido

print("Estes es mi nombre complete: " + nombre_completo)
"""
"""Fin del primer ejercicio en python """
"""
print("1", "2", "3", "4", "5", sep="-")
nombre = "Danny Elian"
Apellido = "Medina Cuello"

nombre_completo = nombre + " " + Apellido
print(nombre_completo, end=".")
"""

"""riables de tipo texto"""
'''
nombre = "Danny Elian"

"""variables de tipo numerico"""
edad = 20

"""variables de tipo booleano"""
verificado = True

"""variables de tipo lista"""
lista = [1, 2, 3, 4, 5]


"""variables de tipo tupla"""
tupla = (1, 2, 3, 4, 5)

""" variables tipo diccionario"""

"""variables de tipo diccionario"""
diccionario = {"nombre": "Danny Elian", "edad": 20, "telefono": 8888888888}

print(diccionario["nombre"], diccionario["edad"])

print(
    """Esto es un str multilinea 

creo yo. """
)

print(None)
'''
# nombre = "Danny Elian"
# apellido = "Medina Cuello"

# apellido = apellido.replace("C", "P")

# print(f"{nombre} y el mejor apellido es: {apellido}")


# texto = "memeememememememememememememememjaefbiyusfisba Elian"
# print(texto)
# texto = texto.replace("memeememememememememememememememjaefbiyusfisba", "Danny")
# print("p" in texto)

# print('elian "Medina"')


# numImaginario = 5j + 3

# print(numImaginario)

# print(1 % 3)


import math

# print(round(1.3))

# print(abs(0))

# print(math.ceil(1.2))
# print(math.floor(1.9))

# escribir = input("Escribe algo: ")

# if escribir == "Danny":
#     print("Buenos dias Danny")
# else:

#     print("No eres Danny")

# Elevar a la potencia

base = int(input("Dgite la base: "))
exponente = int(input("Digite el exponente:"))

result = math.pow(base, exponente)

print(f"El resultado de la potencia de los numeros {base} y {exponente} es: {result}")
