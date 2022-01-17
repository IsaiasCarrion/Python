numero = int(input('Proporciona un valor entre 1 y 3: '))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Numero Uno'
elif numero == 2:
    numeroTexto = 'Numero Dos'
elif numero == 3:
    numeroTexto = 'Numero Tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'Numero proporcionado: {numero} - {numeroTexto}')