# numeros_de_usuario = []

"""
numero_introducido = int(input("Introduzca un numero en la lista: "))
numeros_de_usuario.append(numero_introducido)

while input("Desea introducir mas numeros? (S/N) ") == "S":
    numero_introducido = int(input("Introduzca un numero en la lista: "))
    numeros_de_usuario.append(numero_introducido)


print(numeros_de_usuario)
"""

numeros_introducidos = input("Introduzca los numeros separados por coma: ")
numeros_de_usuario = numeros_introducidos.split(",")

numeros_de_usuario = [int(numero) for numero in numeros_de_usuario]

numero_pequenio = numeros_de_usuario[0]
numero_grande = numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:
    if numero_pequenio > numero:
        numero_pequenio = numero

    if numero_grande < numero:
        numero_grande = numero

print("numero grande: {} y numero pequenio: {}".format(
    numero_grande, numero_pequenio))
