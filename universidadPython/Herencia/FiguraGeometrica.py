class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._ancho = ancho
        self._alto = alto

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
