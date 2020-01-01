import re
lista_nombres=[
    'ana',
    'pedro',
    'maria',
    'rosa',
    'sandra',
    'betob',
    'celia'
]

print("->Imprime un rango de letras ejemplo: nombres que inicia con 'a' o 'b' o 'c'------------------------>")
for elemento in lista_nombres:
    if re.findall('^[a-c]', elemento):
        print(elemento)

print("->Imprime un rango de letras ejemplo: nombres que terminan con 'a' o 'b' o 'c'------------------------>")
for elemento in lista_nombres:
    if re.findall('[a-c]$', elemento):
        print(elemento)

