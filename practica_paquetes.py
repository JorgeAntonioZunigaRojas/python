# Son directorios dende se almacenan modulos relacionados entre si
# Sirven para organizar y reutilizar los modulos
# Pasos para crear un paquete
# --> 1-Crear una carpeta dentro del sitio de trabajo
# --> 2-Crear un archivo __ini__.py para indicar a pyton que la carpeta que la contendra sera un paquete.
from paquete_calculos.practica_paquete_modulo import sumar
print(sumar(8,5))