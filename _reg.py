# # Expresiones regulares
# 1-Import re
from ast import pattern

import re

# # 2- Crear un patron, que es una cadena dque describe lo que queremos encontrar

# pattern = "Free Fire"

# # 3- Texto donde queremos buscar
# text = "Free Fire in battle royale style"

# # 4- Funcion de busqueda de Re
# match = re.search(pattern, text)

# if match:
#     print("Palabra encontrada.")

# else:
#     print("Palabra no encontrada.")

# # .group() devuelve la cadena que coincide con el pattern
# print(match.group())

# # .start() devuelve la pasisicon inicial del match
# print(match.start())

# # .end() devuelve la pasisicon final del match
# print(match.end())

# Consejo del dia


text = "Enfócate en el presente y mantén una actitud positiva actituda"
pattern = "actitud"
# search_dia = re.search(pattern, text)

# if search_dia:
#     print("Palabra encontrada.")
# else:
#     print("Palabra no encontrada.")

# print(
#     f"He encontrado la palabra en la posicion {search_dia.start()} del texto y esta misma termina en la posicion {search_dia.end()} del texto"
# )


result = re.findall(pattern, text)

print(len(result))

result = re.finditer(pattern, text)

for i in result:

    print(i.group(), i.start(), i.end())


# Buscar con distincion de mayusculas y minusculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)


if found:
    print(found)

else:
    print("Not found")


### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto


# text = 'Cherry-pick es como "copiar y pegar" un commit específico de una rama a otra o como duplicar.'

# pattern = "como"

# replacement = "like"

# new = re.sub(pattern, replacement, text, flags=re.IGNORECASE, count=3)

# print(new)

###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

# 1- punto

# Coincidir con cualquier caracter excepto una linea (r)

text = """El niño dijo "hola", luego gritó "holass", después escribió "holla" y finalmente suspiró "hona" cuando quería decir "haya"."""

pattern = r"ho.a"  # prefijo (r)

found = re.findall(pattern, text)

if found:
    print(found)
else:
    print("Palabra no encontrada.")

# Barra invertida para buscar el punto(.)

text = "Mi vida es buena. La tuya tambien..."

pattern = r"\."

found = re.findall(pattern, text)

if found:
    print(found)

else:
    print("Lo sentimos...")
##############################################################

# \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
found = re.findall(r"\d{9}", text)

print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +1 688999999 apúntalo vale?"
pattern = r"\+1 \d{9}"

found = re.search(pattern, text)

if found:
    print(f"El numero: {found.group()}, es un numero de RD")
else:
    print("El numero no es de RD")


# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)
