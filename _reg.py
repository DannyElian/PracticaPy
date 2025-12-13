# # Expresiones regulares
# 1-Import re
from ast import pattern
from operator import le
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


text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found:
    print(found)
