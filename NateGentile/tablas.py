"""
# Numero elegido por el usuario: 2, output esperado:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 11
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24
"""

numero = int(input("Ingresa un numero para ser multiplicado: "))

for factor in range(1, 13):
    # if factor % 2 == 0:
    print("{} x {} = {}".format(numero, factor, numero * factor))
