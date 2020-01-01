def areaCuadrado(lado):
    """Calcula el area de un cuadrado: Elevando al cuadrado el lado pasado por parametro"""
    return  "El area del cuadradp es " + str(lado*lado)

def areaTriangulo(base, altura):
    '''Calcula el area de un triangulo: Utilizando los parametros base y altura
    Segunda linea de comentario que se mostrara en la documentacion y la ayuda de la funcion.
    '''
    '''1era linea de comentario que no se mostrara en la documentacion ni en la ayuda de la funcion
    2da linea de comentario que no se mostrara en la documentacion ni en la ayuda de la funcion
    '''
    return "El area del triangulo es: "+str((base*altura)/2)

print("-------------------------------------------------------\nEjecutando la funcion: areaCuadrado")
print("-->",areaCuadrado(5))
print("-------------------------------------------------------\nImprimiendo la documentacion de la funcion: areaCuadrado")
print("-->",areaCuadrado.__doc__)
print("-------------------------------------------------------\nImprimiendo la ayuda de la funcion: areaCuadrado")
help(areaCuadrado)
print("-------------------------------------------------------")


print("*******************************************************")
print("-------------------------------------------------------\nEjecutando la funcion: areaTriangulo")
print("-->",areaTriangulo(2,7))
print("-------------------------------------------------------\nImprimiendo la documentacion de la funcion: areaTriangulo")
print("-->",areaTriangulo.__doc__)
print("-------------------------------------------------------\nImprimiendo la ayuda de la funcion: areaTriangulo")
help(areaTriangulo)
print("-------------------------------------------------------")