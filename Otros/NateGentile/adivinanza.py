import random

numero_ganador = random.randint(0, 10)
numero_elegido = int(input("Ingresa el numero q tu creas: "))

if numero_elegido == numero_ganador:
    print("En hora buena adivinaste")

print("fallaste vuelve a intentarlo")

print("El numero ganador era: {}".format(numero_ganador))
