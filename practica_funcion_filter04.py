class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "Nombre: {}, Cargo: {}, Salario: {}".format(self.nombre, self.cargo, self.salario)

ListaEmpleados=[
    Empleado("Juan","Director", 750000),
    Empleado("Ana","Presidenta", 850000),
    Empleado("Antonio","Administradorr", 250000),
    Empleado("Sara","Secretaria", 270000),
    Empleado("Mario","Botones", 210000),
]
salarios_altos=filter((lambda empleado: empleado.salario>500000), ListaEmpleados)
for empleado in salarios_altos:
    print(empleado)
