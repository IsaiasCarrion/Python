from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado

teclado1 = Teclado('Hp','USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Hp', 15)
computadora1 = Computadora("Hp", monitor1, teclado1, raton1)


teclado2 = Teclado('Acer', 'bluetooth')
raton2 = Raton('Ryzer', 'bluetooth')
monitor2 = Monitor('RedDragon', 'USB')
computadora2 = Computadora("Generica", monitor2, teclado2, raton2)

teclado3 = Teclado('Gamer', 'bluetooth')
raton3 = Raton('Gamer', 'bluetooth')
monitor3 = Monitor('Acer', 50)
computadora3 = Computadora('Notebook', teclado3, raton3, monitor3)

computadora1 = [computadora1, computadora2]
orden1 = Orden(computadora1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)
