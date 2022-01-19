from rich import print


# def listarTerminos(**terminos):
#     for llave, valor in terminos.items():
#         print(f'{llave}: {valor}')


# listarTerminos(IDE='Integrated Develoment Enviroment', PK="Primary Key")

# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)


# nombres = ['Juan', 'Carla', 'Guillermo']

# desplegarNombres(nombres)
# desplegarNombres('Carlos')

# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * factorial(numero-1)


# resultado = factorial(5)

# print(f'El factorial de 5 es {resultado}')


# def imprimir_numero_recursivo(numero):
#     if numero >= 1:
#         print(numero)
#         imprimir_numero_recursivo(numero-1)


# imprimir_numero_recursivo(5)


# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.

# La función se llama calcular_total()

# La función recibe dos parámetros:

# 1. pago_sin_impuesto

# 2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)

# La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.

# Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0

# Los valores los debe proporcionar el usuario y se procesados con la función input, convirtiendolos a tipo float.


# def calcular_total(pago, impuesto):
#     return pago + pago*(impuesto/100)


# pago = float(input('Proporcione el pago sin impuesto: '))
# impuesto = float(input('Proporcione el monto del impuesto: '))
# pago = calcular_total(pago, impuesto)
# print(f'Pago con impuesto: {pago}')


# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

def celcius_fahrenheit(temp):
    return (temp * 9/5)+32


temperatura = float(input('Ingrese la temperatura a convertir a fahrenheit: '))
resultado = celcius_fahrenheit(temperatura)
print(f'La temperatura en fahrenheit es {resultado}')


def fahrenheit_celcius(temp):
    return (temp-32)*5/9


temperatura = float(input('Ingrese la temperatura a convertir a celcius: '))
resultado = fahrenheit_celcius(temperatura)
print(f'La temperatura en fahrenheit es {resultado}')
