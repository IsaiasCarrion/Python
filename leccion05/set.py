planetas = {"Marte", "Venus", "Jupiter"}
print(planetas)

#Largo
print(len(planetas))

#revisar si un elemento esta presente
print('Martes' in planetas)

#Agregas mas elementos
planetas.add('Tierra')
print(planetas)

#No soporta elementos duplicados
planetas.add('Tierra')

#Eliminar elemento 
planetas.remove('Tierra')
print(planetas)

#Eliminar un elemento sin Error
planetas.discard('Jupiter')
print(planetas)

#limpiar todo el set
planetas.clear()
print(planetas)

#Eliminar todo el set
del planetas
print(planetas)