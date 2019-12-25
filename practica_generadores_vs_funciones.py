'''
def funcion_generar_numeros_pares(limite):
    numero=1
    numeros_pares=[]
    while numero<limite:
        numeros_pares.append(numero*2)
        numero=numero+1
    return numeros_pares

resultado=funcion_generar_numeros_pares(10)
print(resultado)
'''

# La diferencia entre un generador y una funcion es
# --> funcion: devuelve todo el resultado de su algorimo con un "return"
# --> Generador: devuelve parte del resultado de su algorimo con un "yield"
# -----> para acceder a todos su resultados deberas usar un bucle repetitivo y usar "next"

'''
def generador_numeros_pares(limite):
    numero=1
    while numero<limite:
        yield numero*2
        numero=numero+1
resultado=generador_numeros_pares(10)
primer_numero_par=next(resultado)
segundo_numero_par=next(resultado)
tercer_numero_par=next(resultado)

print("Primer numero par: {}".format(primer_numero_par))
print("Segundo numero par: {}".format(segundo_numero_par))
print("Tercer numero par: {}".format(tercer_numero_par))
'''

# -->yield from: ayuda e recorrer elementros en una sola linea
def devuelve_ciudades(*ciudades): #Cuando se coloca un "*" (asterisco) delante de un argumento de una funcion estamos indicando que va a recivir un numero indetermindado de argumentos y los va a recibir en forma de tupla
    for elemento in ciudades:
        yield from elemento #Es equivalente a un buble for

ciudades=devuelve_ciudades("Lima", "Trujillo", "Arequipa", "cusco", "VES")
print(next(ciudades))
print(next(ciudades))
print(next(ciudades))
print(next(ciudades))
print(next(ciudades))














