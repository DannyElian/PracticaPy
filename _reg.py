# # # Expresiones regulares
# # 1-Import re
# from ast import pattern

import re
from os import system

if system("clear") != 0:
    system("cls")


# # # # 2- Crear un patron, que es una cadena dque describe lo que queremos encontrar

# # # pattern = "Free Fire"

# # # # 3- Texto donde queremos buscar
# # # text = "Free Fire in battle royale style"

# # # # 4- Funcion de busqueda de Re
# # # match = re.search(pattern, text)

# # # if match:
# # #     print("Palabra encontrada.")

# # # else:
# # #     print("Palabra no encontrada.")

# # # # .group() devuelve la cadena que coincide con el pattern
# # # print(match.group())

# # # # .start() devuelve la pasisicon inicial del match
# # # print(match.start())

# # # # .end() devuelve la pasisicon final del match
# # # print(match.end())

# # # Consejo del dia


# # text = "Enfócate en el presente y mantén una actitud positiva actituda"
# # pattern = "actitud"
# # # search_dia = re.search(pattern, text)

# # # if search_dia:
# # #     print("Palabra encontrada.")
# # # else:
# # #     print("Palabra no encontrada.")

# # # print(
# # #     f"He encontrado la palabra en la posicion {search_dia.start()} del texto y esta misma termina en la posicion {search_dia.end()} del texto"
# # # )


# # result = re.findall(pattern, text)

# # print(len(result))

# # result = re.finditer(pattern, text)

# # for i in result:

# #     print(i.group(), i.start(), i.end())


# # # Buscar con distincion de mayusculas y minusculas

# # text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
# # pattern = "IA"
# # found = re.findall(pattern, text, re.IGNORECASE)


# # if found:
# #     print(found)

# # else:
# #     print("Not found")


# # ### Reemplazar el texto

# # # .sub() reemplaza todas las coincidencias de un patrón en un texto


# # # text = 'Cherry-pick es como "copiar y pegar" un commit específico de una rama a otra o como duplicar.'

# # # pattern = "como"

# # # replacement = "like"

# # # new = re.sub(pattern, replacement, text, flags=re.IGNORECASE, count=3)

# # # print(new)

# # ###
# # # 02 - Meta caracteres
# # # Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
# # ###

# # # 1- punto

# # # Coincidir con cualquier caracter excepto una linea (r)

# # text = """El niño dijo "hola", luego gritó "holass", después escribió "holla" y finalmente suspiró "hona" cuando quería decir "haya"."""

# # pattern = r"ho.a"  # prefijo (r)

# # found = re.findall(pattern, text)

# # if found:
# #     print(found)
# # else:
# #     print("Palabra no encontrada.")

# # # Barra invertida para buscar el punto(.)

# # text = "Mi vida es buena. La tuya tambien..."

# # pattern = r"\."

# # found = re.findall(pattern, text)

# # if found:
# #     print(found)

# # else:
# #     print("Lo sentimos...")
# # ##############################################################

# # # \d: coincide con cualquier dígito (0-9)

# # text = "El número de teléfono es 123456789"
# # found = re.findall(r"\d{9}", text)

# # print(found)

# # # Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

# # text = "Mi número de teléfono es +1 688999999 apúntalo vale?"
# # pattern = r"\+1 \d{9}"

# # found = re.search(pattern, text)

# # if found:
# #     print(f"El numero: {found.group()}, es un numero de RD")
# # else:
# #     print("El numero no es de RD")


# # # \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

# # text = "el_rubius_69"
# # pattern = r"\w"
# # found = re.findall(pattern, text)
# # print(found)


# # # \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)
# # text = "Hola mundo\n¿Cómo estás?\t"
# # pattern = r"\s"
# # matches = re.findall(pattern, text)
# # print(matches)

# # # ^: Coincide con el principio de una cadena
# # username = "423_name%22"
# # pattern = r"^\w"  # validar nombre de usuario

# # valid = re.search(pattern, username)

# # if valid:
# #     print("El nombre de usuario es válido")
# # else:
# #     print("El nombre de usuario no es válido")

# # phone = "+34 688999999"
# # pattern = r"^\+\d{1,3} "

# # valid = re.search(pattern, phone)

# # if valid:
# #     print("El número de teléfono es válido")
# # else:
# #     print("El número de teléfono no es válido")


# # text = """El niño dijo "hola", luego gritó "holass", después escribió "holla" y finalmente suspiró "hona" cuando quería decir "haya"."""

# # pattern = input("Escribe lo que quieres buscar: ")

# # found = re.search(pattern, text)

# # if found:

# #     print(f"Se encontro la palabra {found.group()} en el texto")

# # else:
# #     print("No se encontro nd en el texto.")


# # phone = input("Digite su telefono: ")

# # pattern = r"^\+\d{1,4}"

# # found = re.search(pattern, phone)

# # if found:
# #     print("Es un numero de telefono")
# # else:
# #     print("NO es un numero de telefono")


# # EJERCICIO:
# # Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt

# files = "file1.txt file2.pdf midu-of.webp secret.txt"
# pattern = r"\w+.txt"

# match = re.findall(pattern, files)
# # print(match)
# if match:
#     print(f"los archivos txt en la lista son: {match}")
# else:
#     print("no")

#     # \b: Coincide con el principio o final de una palabra
# text = "casa casada cosa cosas casado casa"
# pattern = r"\bc.sa\b"

# found = re.findall(pattern, text)
# print(found)


# text = "mama maaaaama mema maaa"
# pattern = r"\bm.ma\b"

# found = re.findall(pattern, text)
# print(found)


# # |: Coincidr con una opción u otra
# fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
# pattern = r"palta|aguacate|p..a|\b\w{7}\b"

# matches = re.findall(pattern, fruits)
# print(matches)


# # Ejercicio 1:
# # ¿Cuantas palabras tienen de 0 a más "a" y después una b?

# text = "bbbadddd aaa ccc a abb aa casaaaaaabb"

# pattern_a = r"a*?b"

# match_a = re.findall(pattern_a, text)

# print(match_a)


# # Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
# phone = input("Digite el numero: ")

# pattern = r"\+?34 | ?00 \d{9}"

# m = re.search(pattern, phone)

# if m:
#     print(m.group())
# else:
#     print("no")

# # {n} cantidad de veces

# text = "bbbadddd aaa ccc a abb aa casaaaaaabb"
# pattern = r"a{2}"

# match = re.findall(pattern, text)

# print(match)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"

match = re.findall(pattern, words)

print(match)
# principio (^) a fin ($)
