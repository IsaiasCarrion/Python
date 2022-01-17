print('Proporciona los siguientes datos del libro')
nombre = input('Proporciona el nombre: ')
id = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio: '))
envioGratuito = input('Indica si el envio es gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto debe escribir True o False'

print(f'''
    Nombre: {nombre}
    ID: {id}
    precio: {precio}
    Envio Gratuito: {envioGratuito}    
 ''')