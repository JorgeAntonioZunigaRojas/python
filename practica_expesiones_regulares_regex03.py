import re
lista_nombres=[
    'hombres',
    'mujeres',
    'nido',
    'cuadernillo',
    'invierno',
    'mascotas',
    'niños',
    'niñas',
    'niñito',
    'camion',
    'camión',
]
print("->Imprime todo elemento que contenga la cadena [ni]------------------------>")
for elemento in lista_nombres:
    if re.findall('ni', elemento):
        print(elemento)
print("->Imprime todo elemento que contenga la cadena [in]------------------------>")
for elemento in lista_nombres:
    if re.findall('in', elemento):
        print(elemento)
print("->Imprime todo elemento que contenga el caracter [n] o [i]------------------------>")
for elemento in lista_nombres:
    if re.findall('[ni]', elemento):
        print(elemento)

print("->Imprime todo elemento que contenga la cadena [niñ]------------------------>")
for elemento in lista_nombres:
    if re.findall('niñ', elemento):
        print(elemento)

print("->Imprime todo elemento que contenga la cadena [niños] o [niñas]------------------------>")
for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)

print("->Imprime todo elemento que contenga la cadena [camion] o [camión]------------------------>")
for elemento in lista_nombres:
    if re.findall('cami[oó]n', elemento):
        print(elemento)

