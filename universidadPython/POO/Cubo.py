class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundidad


base = int(input('Ingresar la base: '))
altura = int(input('Ingresar la altura: '))
profundidad = int(input('Ingresar la profundidad: '))

rubik = Cubo(base, altura, profundidad)

print(f'El cubo rubik tiene un volumen de : {rubik.calcular_volumen()}')
