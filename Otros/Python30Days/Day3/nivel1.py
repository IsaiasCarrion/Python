import math

'''
edad = 33
altura = 1, 77

print(edad, altura)
'''

# Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo (área = 0,5 xbxh).

'''
def area(base, altura):
    return 0, 5 * base * altura


altura = int(input('Ingresar la altura: '))
base = int(input('Ingresa la base: '))

print(area(base, altura))
'''

# Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c).

'''

def perimetro(ladoA, ladoB, ladoC):
    return ladoA + ladoB + ladoC

ladoA = int(input('Ingrese cuanto mide el lado A: '))
ladoB = int(input('Ingrese cuanto mide el lado B: '))
ladoC = int(input('Ingrese cuanto mide el lado C: '))

print(perimetro(ladoA,ladoB,ladoC))
'''

# Obtenga la longitud y el ancho de un rectángulo usando el indicador. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))

'''
longitud = int(input('Ingrese la longitud: '))
ancho = int(input('Ingrese el ancho: '))
area = longitud * ancho
perimetro = (longitud + ancho) * 2
print(
    f'el area del rectangulo es: {area} y el perimetro del rectangulo es: {perimetro}')
'''

# Obtenga el radio de un círculo usando el indicador. Calcula el área (área = pi xrxr) y la circunferencia (c = 2 x pi xr) donde pi = 3,14.
'''
radio = int(input('Ingresar el radio del circulo: '))
pi = math.pi
area = pi*radio*2
circunferencia = 2 * pi * radio
print(f'el area del circulo es: {area} y su circunferencia es: {circunferencia}')
'''

# Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación falsa.
'''
longitudpy = 'python'
longituddr = 'dragon'
compare = longituddr == longitudpy
print(compare)
'''

# Use un operador para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
'''
result = longituddr and longitudpy
print(result)
'''

# Espero que este curso no esté lleno de jerga . Use el operador in para verificar si hay jerga en la oración.
'''
oracion = 'Espero que este curso no este lleno de jerga'
resultado = oracion in 'jerga'
print(resultado)
'''

# Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
'''
texto = 'python'
length = float(len(texto))
string = str(length)
print(length, string)
'''

# Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?

'''
numeros = 11

while numeros < 11:
    if numeros % 2 == 0:
        print(numeros)
    numeros += 1

for numeros in range(0, 11, 2):
    print(numeros)

print([i for i in range(0, 11) if i % 2 == 0])


def generarPares(m):
    n = 0
    lista = []
    while n < m:
        lista.append(n*2)
        n += 1
    return lista


print(generarPares(6))
'''

# verifique si la división del piso de 7 por 3 es igual al valor int convertido de 2.7.
'''
comparacion = 2 * 7 == 7 * 3
print(comparacion)
'''

# Compruebe si el tipo de '10' es igual al tipo de 10
'''
diez = 10
diez_str = '10'
comp = diez == diez_str
print(comp)
'''

# Comprueba si int('9.8') es igual a 10
'''
test = int(9.8)
prueba = 10
ver = test == prueba
print(ver)
'''

# Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?
'''
horas = int(input('Ingrese las horas: '))
tarifa = int(input('Ingrese la tarifa por hora: '))
salario = horas * tarifa
print(f'su salario es de : {salario}')
'''

# Escriba un script que solicite al usuario que ingrese el número de años. Calcular el número de segundos que puede vivir una persona. Supongamos que una persona puede vivir cien años.
'''
años = int(input('Ingrese numeros de años: '))
segundos = 31536000
resultado = años * segundos
print(f'has vivido {resultado} segundos de vida')
'''

# Escriba un script de Python que muestre la siguiente tabla
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
lista = [['1', '1', '1', '1', '1'],
         ['2', '1', '2', '4', '8'],
         ['3', '1', '3', '9', '27'],
         ['4', '1', '4', '16', '65'],
         ['5', '1', '5', '25', '125']]

print(lista)
