#Definir una lista tipo str
nombres = ['Juan', 'Carla', 'Ricardo', 'Maria']
#Imprimir la lista de nombres
print(nombres)

#Acceder a elementos de manera individual
print(nombres[0])
print(nombres[1])

#Accerder a los elementos de manera inversa
print(nombres[-1])

#Imprimir un rango
print(nombres[0:2])

#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])

#Desde el indice indicado hasta el final
print(nombres[1:])

#Cambiar valor
nombres[3] = 'Ivone'
print(nombres)

#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existe mas nombre en la lista')

#Preguntar el largo de una lista
print(len(nombres))

#Agregar un elemento
nombres.append('Lorenzo')
print(nombres)

#Insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)

#Remove elemento
nombres.remove('Octavio')
print(nombres)

#Remover el ultimo valor agregado
nombres.pop()
print(nombres)

#Eliminar un indice
del nombres[0]
print(nombres)

#Limpiar la lista
nombres.clear()
print(nombres)

#Borrar la lista por completo
del nombres
print(nombres)