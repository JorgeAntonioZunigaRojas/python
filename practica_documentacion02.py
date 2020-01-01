from paquete_calculos import practica_paquete_modulo

class Areas:
    """
    Esta clase calcula el area de las diferentes figuras geometricas
    """
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

print("-------------------------------------------------------\nEjecutando del metodo: areaCuadrado")
print("-->",Areas.areaCuadrado(5))
print("-------------------------------------------------------\nImprimiendo la documentacion del metodo: areaCuadrado")
print("-->",Areas.areaCuadrado.__doc__)
print("-------------------------------------------------------\nImprimiendo la ayuda del metodo: areaCuadrado")
help(Areas.areaCuadrado)
print("-------------------------------------------------------")


print("*******************************************************")
print("-------------------------------------------------------\nEjecutando del metodo: areaTriangulo")
print("-->",Areas.areaTriangulo(2,7))
print("-------------------------------------------------------\nImprimiendo la documentacion del metodo: areaTriangulo")
print("-->",Areas.areaTriangulo.__doc__)
print("-------------------------------------------------------\nImprimiendo la ayuda del metodo: areaTriangulo")
help(Areas.areaTriangulo)
print("-------------------------------------------------------")
print("*******************************************************")
help(Areas)
help(practica_paquete_modulo)