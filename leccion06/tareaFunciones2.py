def mult_valores(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado

print(mult_valores(3,5))
