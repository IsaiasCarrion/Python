class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'Figura geometrica[Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False


for ran in range(1, 101):
    divisibleXTres = ran % 3 == 0
    divisibleXCinco = ran % 5 == 0
    if (divisibleXTres and divisibleXCinco):
        print("FizzBuzz")
    elif divisibleXTres:
        print("Fizz")
    elif divisibleXCinco:
        print("Buzz")
    else:
        print(ran)
