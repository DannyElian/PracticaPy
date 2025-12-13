# Expresiones regulares
# 1-Import re
from ast import pattern
import re

# 2- Crear un patron, que es una cadena dque describe lo que queremos encontrar

pattern = "Free Fire"

# 3- Texto donde queremos buscar
text = "Free Fire in battle royale style"

# 4- Funcion de busqueda de Re
match = re.search(pattern, text)

if match:
    print("Palabra encontrada.")

else:
    print("Palabra no encontrada.")

# .group() devuelve la cadena que coincide con el pattern
print(match.group())

# .start() devuelve la pasisicon inicial del match
print(match.start())

# .end() devuelve la pasisicon final del match
print(match.end())
