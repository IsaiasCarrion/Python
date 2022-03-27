"""
# Ejemplo:
texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"
espacios = [" "]
puntos = ["."]
comas = [","]
espacios_count = 0
puntos_count = 0
comas_count = 0

for text in texto_usuario:
    if text in espacios:
        print("He encontrado {}".format(text))
        espacios_count +=1
    elif text in puntos:
        print("He encontrado {}".format(puntos))
        puntos_count += 1
    elif text in comas:
        print("He encontrado {}".format(comas))
        comas_count += 1

print("Se encontraron {} espacios".format(espacios_count))
print("Se encontraron {} puntos".format(puntos_count))
print("Se encontraron {} comas".format(comas_count))
"""

texto_usuario = input("Introduzca un texto: ")
espacios = 0
puntos = 0
comas = 0

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("Espacios {}, Puntos {}, Comas {}".format(espacios, puntos, comas))
