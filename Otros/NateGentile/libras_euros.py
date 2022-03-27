dolar_euro = 0.90
euro_dolar = 1.11
libra_euro = 1.20
euro_libra = 0.83

opcion = input("Que desea Hacer? \n"
               "A - Convertir de dolar a euro\n"
               "B - Convertir de euro a dolar\n"
               "C - Convertir de libra a euro\n"
               "D - Convertir de euro a libra\n:")

texto_usuario = "Introduzca la cantidad de {} a convertir: "

if opcion == "A":
    dinero = float(input(texto_usuario.format("dolares")))
    print(("Los Dolares a Euro son: {}").format(dinero * dolar_euro))

elif opcion == "B":
    dinero = float(input(texto_usuario.format("dolares")))
    print(("Los Dolares a Euro son: {}").format(dinero * euro_dolar))

elif opcion == "C":
    dinero = float(input(texto_usuario.format("dolares")))
    print(("Los Dolares a Euro son: {}").format(dinero * libra_euro))

elif opcion == "D":
    dinero = float(input(texto_usuario.format("dolares")))
    print(("Los Dolares a Euro son: {}").format(dinero * euro_libra))

else:
    print("Las opciones ingresadas no son correctas")
