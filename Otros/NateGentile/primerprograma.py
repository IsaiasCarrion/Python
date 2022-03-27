
'''
a = 2
print(a)

a = a * 2
print(a)

a = "hola"
print(a)

print(a * 3)

nombre = input('Cual es tu nombre?: ')
print('Tu nombre es: ' + nombre)

maximoValor = max(1, 2, 3, 4)
print(maximoValor)
'''

a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))
c = int(input('Ingrese el tercer numero: '))

maximo_valor = max(a, b, c)
minimo_valor = min(a, b, c)

print("El numero mas grande entre {}, {} y {} es: {} y el minimo {}".format(a, b, c,
                                                                            max(a,
                                                                                b, c),
                                                                            min(a, b, c)))

print(f'el maximo valor es {maximo_valor}')
print(f'el minimo valor es {minimo_valor}')
