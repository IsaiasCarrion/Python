# class Persona:
#     def __init__(self):
#         self.nombre = 'Juan'
#         self.apellido = 'Perez'
#         self.edad = 28

# persona1 = Persona()
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()
# Persona.mostrar_detalle(persona1)
# print(f'Objeto Persona 1 {persona1.nombre} {persona1.apellido} {persona1.edad}')

# persona1.nombre = 'Juan Carlos'
# persona1.apellido = 'Juarez'
# persona1.edad = 25
# print(f'Objeto Persona 1 {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()
# print(f'Objeto Persona 2 {persona2.nombre} {persona2.apellido} {persona2.edad}')

# persona2.nombre = 'Macarena'
# persona2.apellido = 'Alderete'
# persona2.edad = 28
# print(f'Objeto Persona 2 {persona2.nombre} {persona2.apellido} {persona2.edad}')
