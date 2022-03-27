tpl_vacia = []
tlp_hermanas = ('Macarena', 'Carla', 'Maria')
tlp_hermanos = ('Isaias', 'Isamael', 'David')
tlp_hemanos_all = tlp_hermanas + tlp_hermanos
print(tlp_hemanos_all)

print(len(tlp_hemanos_all))

# Transformo las tuplas a listas
lstHermanos = list(tlp_hermanos)
lstHermanas = list(tlp_hermanas)

# Agrego Padre y Madre a las listas
lstHermanos.append('Padre')
lstHermanas.append('Madre')

# Concateno las listas y mando a imprimirlas juntas como familyMembers
familyMembers = lstHermanas + lstHermanos
print(familyMembers)

