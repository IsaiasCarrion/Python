edad = int(input('Proporcina tu edad: '))
mensaje = None

if 0 <= edad < 10:
    mensaje = 'La infancia es hermosa'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios, mucho estudio'
elif 20 <= edad < 30:
    mensaje = 'Amor mucho trabajo'
else:
    mensaje = 'Edad no reconocida'
print(f'Tu edad es: {edad}, {mensaje}')
    