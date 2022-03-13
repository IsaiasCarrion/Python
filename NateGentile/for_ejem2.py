"""
# Ejemplo:
texto_usuario: "Hola me llamo Isa. ¿Tu como te LLamas?"

# Output

masyusculas = 3 
"""

import string

texto_usuario = input(" Introduzca un texto: ")
letras_mayusculas = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print("Las mayusculas son : {}".format(letras_mayusculas))
