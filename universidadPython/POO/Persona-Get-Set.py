class Persona:
    def __init__(self, nombre, apellido, edad,):  # *valores, **terminos
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property 
    def nombre(self):
        print('llamando metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('llamando metodo set')
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona ('Juan','Perez', 28)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
# persona1._nombre = 'Cambio'
# print(persona1._nombre)

