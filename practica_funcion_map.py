class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "Nombre: {}, Cargo: {}, Salario: {}".format(self.nombre, self.cargo, self.salario)

ListaEmpleados=[
    Empleado("Juan","Director", 6700),
    Empleado("Ana","Presidenta", 7500),
    Empleado("Antonio","Administradorr", 2100),
    Empleado("Sara","Secretaria", 2150),
    Empleado("Mario","Botones", 1800),
]
def calcular_comision(empleado):
    if empleado.salario<3000:
        empleado.salario=empleado.salario*1.03

    return empleado

Lista_Empleados_Comision=map(calcular_comision, ListaEmpleados) # La funcion "map" aplica la funcion "calcular_comision" a cada elemento de la lista "ListaEmpleados"

for comision in Lista_Empleados_Comision:
    print(comision)
