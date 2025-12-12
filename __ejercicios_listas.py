from os import system

if system("clear") != 0:
    system("cls")
# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

listOne = [1, 2, 3, 4, 5]
listOne.append(6)
listOne.insert(2, 10)
listOne[0] = 0
print(listOne)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

listTwo_a = [1, 2, 3]
listTwo_b = [4, 5, 6, 1, 2]

listTwo_a.extend(listTwo_b)
listTwo_a.remove(1)
r = listTwo_a.pop(3)
print(r)
print(listTwo_a)

listTwo_b.clear()
print(listTwo_b)
# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

listThree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del listThree[2:5]
print(listThree)

#  Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

listFour = [5, 2, 8, 1, 9, 4, 2]
listFour.sort()
sort = listFour.count(2)
seven = 7 in listFour
print(sort)
print(listFour)
print(seven)

fruits = ["Manzana", "Pera", "Pina"]
for index, fruit in enumerate(fruits):
    print(f"el indice es: {index} y la fruta es:{fruit}")

firstNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
secondNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for f in firstNumber:
    for s in secondNumber:
        r = f * s

        print(f"{f}x{s} = {r}")

fruits2 = ["Manzana", "Pera", "Pina"]

# Comprension de listas
fruit_lower = [fru.lower() for fru in fruits2]

print(fruit_lower)


# Numeros pares de la lista
pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prt = [n for n in pares if n % 2 == 0]

print(prt)

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:

    print(n)

for n in range(1, 11):
    print(n)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

for n in range(1, 21, 2):

    print(n)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

for n in range(5, 51, 5):

    print(n)

    # Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

for n in range(10, 0, -1):

    print(n)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
sum = 0
for n in range(1, 101):
    sum += n
    print(sum)

    # Ejercicio 6: Tabla de multiplicar
    # Pide al usuario que introduzca un número.
    # Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
# print("\nEjercicio 6:")
# num = int(input("Ingrese un numero: "))
# for n in range(1, 13):
#     print(f"{num} x {n} = {(n * num)}")


def generar_tabla_de_multiplicar():
    print("\nEjercicio 6:")
    num = int(input("Ingrese un numero: "))
    for n in range(1, 13):
        print(f"{num} x {n} = {(n * num)}")


print("Generador de tablas de multiplicar: ")
generar_tabla_de_multiplicar()


def sumar(a, b):
    return a + b


print(sumar(2, 3))


def decribir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} y mi genero es {sexo}")


print(decribir_persona("Elian", 20, "M"))

print(decribir_persona(20, "elian", "m"))
print(decribir_persona(edad=20, nombre="elian", sexo="m"))


def sumar_numeros_infinitos(*args):
    # Sumar numeros infinitos con *args
    suma = 0
    for n in args:
        suma += n

    return suma


print(sumar_numeros_infinitos(2, 3, 4, 5, 6, 7))


# Argumentos por clave de valor variable
def mostrar_info_variable(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mostrar_info_variable(nombre="elian")
print("")
mostrar_info_variable(nombre="elian", apellido="Medina", edad=20)
