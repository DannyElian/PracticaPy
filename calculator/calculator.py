# Calculadora
import model

model.Menu()

r = 0
while r >= 0:
    r = int(input("Selecciona tu operacion: "))
    if (r) == 1:

        print("Haz elegido sumar 2 numeros. \n")
        model.SumarDosNumero()
        print("")
        print(
            """1- para volver al menu de inicio
2- para salir del sistema"""
        )
        print("")
        r = int(input("Que quiere hacer: "))

        if (r) == 1:
            model.Menu()
            continue

        else:
            print("Saliste del sistema.")
        break

    elif (r) == 2:

        print("Haz elegido restar 2 numeros. \n")
        model.RestarDosNumero()
        print(
            """1- para volver al menu de inicio
2- para salir del sistema"""
        )
        r = int(input("Que quiere hacer: "))
        if (r) == 1:
            model.Menu()
            continue
        else:
            print("Saliste del sistema.")
        break

    elif (r) == 3:

        print("Haz elegido dividir 2 numeros. \n")
        model.DividirDosNumero()
        print(
            """1- para volver al menu de inicio
2- para salir del sistema"""
        )
        r = int(input("Que quiere hacer: "))
        if (r) == 1:
            model.Menu()
            continue
        else:

            print("Saliste del sistema.")
            break

    elif (r) == 4:

        print("Haz elegido multiplicar 2 numeros. \n")
        model.MultiplicarDosNumero()
        print(
            """1- para volver al menu de inicio
2- para salir del sistema"""
        )
        r = int(input("Que quiere hacer: "))
        if (r) == 1:
            model.Menu()
            continue
        else:
            print("Saliste del sistema.")
            break
    elif r == 5:
        print("Haz elegido Potenciar 2 numeros. \n")
        model.PotenciarDosNumero()
        print(
            """1- para volver al menu de inicio
2- para salir del sistema"""
        )
        r = int(input("Que quiere hacer: "))
        if (r) == 1:
            model.Menu()
            continue
        else:

            print("Saliste del sistema.")
            break

    elif (r) == 0:
        print("Saliste del sistema")
        break

    elif not r == 0 or 1 or 2 or 3 or 4 or 5:

        print("")
        print(f"Digitaste un numero incorrecto \nvolver a intentar \n")
        model.Menu()
        continue
