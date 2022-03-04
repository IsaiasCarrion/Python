opcion = input("¿[A]Android o [I]iOS: ")

movil_ideal = "Ninguno"

if opcion == "A":
    opcion = input("Tienes dinero [S/N]")

    if opcion == "S":
        opcion = input("Te importa la camara del movil [S/N]")

        if opcion == "S":
            movil_ideal = "Google pixel supercam"

        else:
            movil_ideal = "Android calidad-precio"

if opcion == "I":
    opcion = input("Tienes dinero [S/N]")

    if opcion == "S":
        movil_ideal = "iPhone Pro Max"
    else:
        movil_ideal = "Iphone segunda mano"

print("Tu movil ideal es: " + movil_ideal)