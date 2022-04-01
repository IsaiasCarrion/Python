archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())

# Leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))


# Iterar un archivo
# for linea in archivo:
#    print(linea)


# Leer lineas
# print(archivo.readlines())

# Acceder a una linea de la lista

# with open('prueba.txt', 'r', encoding='utf8') as archivo:
# Acceder a una linea de la lista
# print(archivo.readlines()[0])


# Abrimos un nuevo archivo
# a - Anexar informacion
archivo2 = open('copia.txt', 'a')

archivo2.write(archivo.read())
archivo.close()
archivo2.close()
print('Se termino')
