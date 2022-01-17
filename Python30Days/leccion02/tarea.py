edadAdulto = 18
edadPersona = int(input('Proporciona tu edad: '))

if edadPersona > edadAdulto:
    print('eres mayor de edad')
else:
    print(f'no eres mayor de edad {edadPersona}')