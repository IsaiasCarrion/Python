from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        {self._nombre}:{self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        """
        
teclado1 = Teclado('Hp','USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Hp', 15)
computadora1 = Computadora("Hp", monitor1, teclado1, raton1)
print(computadora1)

teclado2 = Teclado('Acer', 'bluetooth')
raton2 = Raton('Ryzer', 'bluetooth')
monitor2 = Monitor('RedDragon', 'USB')
computadora2 = Computadora("Generica", monitor2, teclado2, raton2)
print(computadora2)
