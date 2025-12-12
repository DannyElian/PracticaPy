import math


def SumarDosNumero():

    n1 = int(input("Ingresa el primer numero: "))

    n2 = int(input("Ingresa el segundo numero: "))

    result = n1 + n2

    print(f"El resultado es: {result}")


def RestarDosNumero():

    n1 = int(input("Ingresa el primer numero: "))

    n2 = int(input("Ingresa el segundo numero: "))

    result = n1 - n2

    print(f"El resultado es: {result}")


def DividirDosNumero():

    n1 = int(input("Ingresa el primer numero: "))

    n2 = int(input("Ingresa el segundo numero: "))

    result = n1 / n2

    print(f"El resultado es: {result}")


def MultiplicarDosNumero():

    n1 = int(input("Ingresa el primer numero: "))

    n2 = int(input("Ingresa el segundo numero: "))

    result = n1 * n2

    print(f"El resultado es: {result}")


def PotenciarDosNumero():
    n1 = int(input("Ingresa el primer numero: "))

    n2 = int(input("Ingresa el segundo numero: "))

    result = math.pow(n1, n2)

    print(f"El resultado es: {result}")


def Menu():
    print("Calculadora basica.")
    print("------------------")

    print("Elige una operacion basica: ")
    print("sumar (1)")
    print("restar (2)")
    print("dividir (3)")
    print("multiplicar (4)")
    print("potenciar (5)")
    print("Salir (0)")
