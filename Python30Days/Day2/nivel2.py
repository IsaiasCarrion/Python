import math
# Dia 2: 30 dias de programacion con Python
nombre = 'micky'
apellido = 'carrion'
nombreCompleto = 'Isaias Carrion'
pais = 'Argentina'
ciudad = 'San Miguel de Tucuman'
edad = 33
is_married = True
is_true = True
is_ligth_on = True

gato, molesto = 'micky','re molesto'
print(gato, molesto)


print(type(nombre))
print(type(edad))
print(type(is_true))
print(len(nombreCompleto))

'''
Declarar 5 como num_one y 4 como num_two
    Agregue num_one y num_two y asigne el valor a un total variable
    Reste num_two de num_one y asigne el valor a una variable diff
    Multiplique num_two y num_one y asigne el valor a un producto variable
    Divide num_one por num_two y asigna el valor a una división variable
    Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un        resto variable
    Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
    Encuentre la división de piso de num_one por num_two y asigne el valor a una variable           floor_division
'''

num_one = 5
num_two = 4

suma = num_one + num_two
resta = num_one - num_two
multiplicacion = num_one * num_two
division = num_one / num_two
modulo = num_one % num_two
potencia = num_one ** num_two 
print(suma, resta, multiplicacion,division,modulo,potencia)

'''
El radio de un círculo es de 30 metros.
Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
Tome el radio como entrada del usuario y calcule el área.
'''

circulo_radio = 30
pi = math.pi
area_of_circle = pi * (circulo_radio ** 2)
circum_of_circle = 2 * pi * circulo_radio
print(area_of_circle,circum_of_circle)

def usuario(nombre, apellido,edad,pais):
    return (f'el usuario {nombre} {apellido} con la edad de {edad}, originario del pais {pais}')

print(usuario('isaias','carrion',33,'Argentina'))

