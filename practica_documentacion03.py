#-> El presente archio muestra como se puede realizar pruebas de las funciones con la documentacion y
#-> usando la libreria [docest] que muestra un reporte con de errores si estos ocurren luego de realizar las pruebas de la documentacion
#-> Las pruebas estan antecedidas de los siguientes caracteres [>>>]
#-> Funcion que retorna un dato numerico

def areaTriangulo(base, altura):
    """
    Calcula el area del triangulo
    areaTriangulo(3,6) el resultado es 9.0 por lo tanto no muestra error.
    areaTriangulo(3,6) el resultado es 13.5 por lo tanto no muestra error.
    areaTriangulo(3,7) el resultado es 10.5 por lo tanto SI muestra error.
    areaTriangulo(3,6) el resultado es 10.0 por lo tanto SI muestra error por que tambien es importante el tipo de dato (entero o decimal).

    >>> areaTriangulo(3,6)
    9.0
    >>> areaTriangulo(9,3)
    13.5
    >>> areaTriangulo(3,7)
    10.0
    >>> areaTriangulo(4,5)
    10

    """
    return base*altura/2

import doctest
doctest.testmod()
