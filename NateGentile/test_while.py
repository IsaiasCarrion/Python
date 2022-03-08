import os
from random import randint


vida_inicial_pikachu = 80
vida_inicial_squirtle = 90
tamaño_vida = 20

vida_pikachu = vida_inicial_pikachu
vida_squirtle = vida_inicial_squirtle

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se desenvuelven los turnos de combate

    # Turno Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola Voltio
        print("Pikachu ataque con bola voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataque Onda Trueno")
        vida_squirtle -= 11

    if vida_squirtle < 0:
        vida_squirtle = 0
    if vida_pikachu < 0:
        vida_pikachu = 0

    # Vida Pokemons
    print("La vida de Pikachu {}, La vida de Squirtle {}".format(
        vida_pikachu, vida_squirtle))

    baras_de_vida_pikachu = int(
        vida_pikachu * tamaño_vida / vida_inicial_pikachu)
    print("Pikachu: [{}{}] ({}/{})".format(
        "*" * baras_de_vida_pikachu, " " * (tamaño_vida - baras_de_vida_pikachu), vida_pikachu, vida_inicial_pikachu))

    baras_de_vida_squirtle = int(
        vida_squirtle * tamaño_vida / vida_inicial_squirtle)
    print("Squirtle: [{}{}] ({}/{})".format(
        "*" * baras_de_vida_squirtle, " " * (tamaño_vida - baras_de_vida_squirtle), vida_squirtle, vida_inicial_squirtle))

    input("Enter para continuar ...")
    os.system("cls")

    # Turno Squirtle
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "T"]:
        ataque_squirtle = input(
            "Que ataque deseas realizar: [P]lacaje, Pistola de [A]gua, [B]urbuja, Pasar [T]urno: ")

    if ataque_squirtle == "P":
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        vida_pikachu -= 9
    elif ataque_squirtle == "T":
        print("Pasaste Turno")

    # Vida Pokemons
    baras_de_vida_pikachu = int(
        vida_pikachu * tamaño_vida / vida_inicial_pikachu)
    print("Pikachu: [{}{}] ({}/{})".format(
        "*" * baras_de_vida_pikachu, " " * (tamaño_vida - baras_de_vida_pikachu), vida_pikachu, vida_inicial_pikachu))

    baras_de_vida_squirtle = int(
        vida_squirtle * tamaño_vida / vida_inicial_squirtle)
    print("Pikachu: [{}{}] ({}/{})".format(
        "*" * baras_de_vida_squirtle, " " * (tamaño_vida - baras_de_vida_squirtle), vida_squirtle, vida_inicial_squirtle))

    input("Enter para continuar ...")
    os.system("cls")

if vida_pikachu > vida_squirtle:
    print("Gana Pikachu")
elif vida_squirtle > vida_pikachu:
    print("Gana Squirtle")
