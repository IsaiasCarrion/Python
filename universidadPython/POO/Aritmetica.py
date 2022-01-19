class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones sumar restar multiplicar dividir 
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def suma(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB

    def division(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(20, 10)
print(aritmetica1.suma())
print(aritmetica1.resta())
print(aritmetica1.multiplicacion())
print(aritmetica1.division())
