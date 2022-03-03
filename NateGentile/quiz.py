'''
¿Cuanto te gusta el queso?

puntuacion = 0

Pregunta 1: ¿Que haces cuando vez una tabla de quesos?

A - Salgo corriendo
B - Pruebo uno de los quesos incluso varios
C - No puedo evitar devorarlos

Pregunta 2: ¿Como te gusta la hamburguesa?

A - Sin queso
B - Con queso
C - Pan y queso

Pregunt 3: ¿Eres intolerante a la lactosa?

A - Si
B - A veces 
C - No

- 30
- 15
- 0 
'''

from unittest import result


titulo = "Bienvenido al test sobre quesos"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Que haces cuando vez una tabla de quesos?\n"
               "A - Salgo corriendo\n"
               "B - Pruebo uno de los quesos incluso varios\n"
               "C - No puedo evitar devorarlos\n")

if opcion == "A":
    puntuacion += 0

elif opcion == "B":
    puntuacion += 5

elif opcion == "C":
    puntuacion += 10

else:
    print("Las opciones ingresadas no son correctas")
    exit()

opcion = input("Pregunta 2: ¿Como te gusta la hamburguesa?\n"
               "A - Sin queso\n"
               "B - Con queso\n"
               "C - Pan y queso\n")

if opcion == "A":
    puntuacion += 0

elif opcion == "B":
    puntuacion += 5

elif opcion == "C":
    puntuacion += 10

else:
    print("Las opciones ingresadas no son correctas")
    exit()

opcion = input("Pregunt 3: ¿Eres intolerante a la lactosa?\n"
               "A - Si\n"
               "B - A veces\n"
               "C - No\n")

if opcion == "A":
    puntuacion += 0

elif opcion == "B":
    puntuacion += 5

elif opcion == "C":
    puntuacion += 10

else:
    print("Las opciones ingresadas no son correctas")
    exit()

if puntuacion >= 25:
    print("Resultado Felicidades eres fanatico de los quesos")

elif puntuacion >= 15:
    print("Resultado Felicidades te gustan los quesos")

else:
    print("Resultado Felicidades no te gusta el queso")

print(puntuacion)
