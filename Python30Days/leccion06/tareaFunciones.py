def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valores(3,5,9))
