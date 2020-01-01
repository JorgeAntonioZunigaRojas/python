import re
lista_nombres=[
    'Ma1',
    'Se2',
    'Ma2',
    'Ba1',
    'Ma3',
    'Va1',
    'Va2',
    'Ma4',
    'Ma5',
    'MaA',
    'MaB',
    'Ma.5',
    'Ma.1',
    'Ma:1',
    'Ma:10'
]

print("->Mostrar: Ma1,Ma2,Ma3------------------------>")
for elemento in lista_nombres:
    if re.findall('Ma[0-3]', elemento):
        print(elemento)

print("->Mostrar: [Ma] pero no mostrar a [Ma1, Ma2, Ma3]------------------------>")
for elemento in lista_nombres:
    if re.findall('Ma[^0-3]', elemento):
        print(elemento)

print("->Mostrar: Ma1,Ma2,Ma3 y MaA, MaB------------------------>")
for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento)

print("->Mostrar: Ma + [.:]------------------------>")
for elemento in lista_nombres:
    if re.findall('Ma[.:]', elemento):
        print(elemento)
