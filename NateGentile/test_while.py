from random import randint

vida_pikachu = 80
vida_squirtle = 90

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

    # Vida Pokemons
    print("La vida de Pikachu {}, La vida de Squirtle {}".format(
        vida_pikachu, vida_squirtle))

    input("Enter para continuar ...")

    # Turno Squirtle
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input(
            "Que ataque deseas realizar: [P]lacaje, Pistola de [A]gua, [B]urbuja: ")

    if ataque_squirtle == "P":
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        vida_pikachu -= 9

    # Vida Pokemons
    print("La vida de Pikachu {}, La vida de Squirtle {}".format(
        vida_pikachu, vida_squirtle))

    input("Enter para continuar ...")

if vida_pikachu > vida_squirtle:
    print("Gana Pikachu")
elif vida_squirtle > vida_pikachu:
    print("Gana Squirtle")
