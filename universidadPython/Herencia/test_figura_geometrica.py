from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(lado=-5, color='rojo')
print(f'Calculo del Area es: {cuadrado1.calcular_area()}')
print(cuadrado1)


rectangulo1 = Rectangulo(ancho=13, alto=8, color='verde')
print(f'Calculo del Area es: {rectangulo1.calcular_area()}')
print(rectangulo1)
# MRO Method Resolution Order

# Cuadrado.mro()
# print(Cuadrado.mro())
