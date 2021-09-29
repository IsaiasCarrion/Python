#Definir una tupla
frutas = ('Naranja','Platano','Guayaba')

#Saber el largo
print(len(frutas))

#Acceder a un elemento
print(frutas[0])

#Navegacion inversa
print(frutas[-1])

#Acceder a un rango
print(frutas[0:1]) # sin incluir el ultimo indice

#Recorrer los elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ')

#Cambiar valor tupla
#frutas[0] = 'Pera'
frutaLista = list(frutas)
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista)

print('\n', frutas)

#Eliminar tupla
del frutas
print(frutas)

