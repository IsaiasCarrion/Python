from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calculo del Area es: {cuadrado1.calcular_area()}')

# MRO Method Resolution Order

Cuadrado.mro()
print(Cuadrado.mro())
