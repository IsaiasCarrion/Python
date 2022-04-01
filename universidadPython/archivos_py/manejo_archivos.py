try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Agregamos texto al archivo\n')
    archivo.write('Adios')
except expression as e:
    print(e)
finally:
    archivo.close()
