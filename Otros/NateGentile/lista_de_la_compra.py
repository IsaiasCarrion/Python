'''
Programa lista de la compra

¿Que desea comprar? ([Q] para salir) > Leche
Seguro q quiere añadir "Leche"? [S/N] > S
Leche Añadida!

La lista de la compra es:
["Leche", "Pan"]
'''

lista_compras = []
input_de_usuario = None

print("Lista de la compra")


while input_de_usuario != "Q":
    input_de_usuario = input("Que desea comprar? ([Q] para salir): ")
    if input_de_usuario == "Q":
        pass
    elif input_de_usuario in lista_compras:
        print("{} esto ya esta en la lista".format(input_de_usuario))
    else:
        if input("Seguro q quiere añadir {} a la lista de la compras? [S/N]: ".format(input_de_usuario)) == "S":
            lista_compras.append(input_de_usuario)


print("La lista de la compra es: ")
print(lista_compras)
