#MetaCaracteres
#-->Anclas y clases de caracteres
import re
lista_nombres=[
    "Ana Gómez",
    "Maria Martin",
    "Sandra Lopez",
    "Santiago Martin",
    "Antonio Zuñiga",
    "Sandra Fernandez",
]
print("== Inicia con [Sandra] =======================================================")
for elemento in lista_nombres:
    if re.findall("^Sandra", elemento): #Imprime si la cadena de caracteres conntenidos en "elemento" inicia con la palabla "Sandra"
        print(elemento)
print("== Termina con [Martin] =======================================================")
for elemento in lista_nombres:
    if re.findall("Martin$", elemento): #Imprime si la cadena de caracteres conntenidos en "elemento" termina con la palabla "Martin"
        print(elemento)
print("== Contiene [ñ] =======================================================")
for elemento in lista_nombres:
    if re.findall("[ñ]", elemento): #Imprime si la cadena de caracteres conntenidos en "elemento" contiene la palabla "ñ"
        print(elemento)
print("== Contiene [ñ] o contiene [i] =======================================================")
for elemento in lista_nombres:
    if re.findall("[ñi]", elemento): #Imprime si la cadena de caracteres conntenidos en "elemento" contiene la letra "ñ" o la letra "i"
        print(elemento)
