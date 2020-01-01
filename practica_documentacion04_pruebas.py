#-> El presente archio muestra como se puede realizar pruebas de las funciones con la documentacion y
#-> usando la libreria [docest] que muestra un reporte con de errores si estos ocurren luego de realizar las pruebas de la documentacion
#-> Las pruebas estan antecedidas de los siguientes caracteres [>>>]
#-> Funcion que retorna un dato cadena de texto

def areaTriangulo(base, altura):
    """
    Calcula el area del triangulo
    areaTriangulo(3,6) el resultado es 'El resultado es: 9.0' por lo tanto no muestra error.
    areaTriangulo(3,6) el resultado es 'El resultado es: 13.5' por lo tanto no muestra error.
    areaTriangulo(3,7) el resultado es 'El resultado es: 10.5' por lo tanto SI muestra error.
    areaTriangulo(3,6) el resultado es 'El resultado es: 10.0' por lo tanto SI muestra error por que una funcion retorna una cadena que inicia y termina  con comillas simples.
    y en la prueba he espera una cadena con comillas dobles....

    >>> areaTriangulo(3,6)
    'El resultado es: 9.0'
    >>> areaTriangulo(9,3)
    'El resultado es: 13.5'
    >>> areaTriangulo(3,7)
    'El resultado es: 10.0'
    >>> areaTriangulo(4,5)
    "El resultado es: 10.0"

    """
    return 'El resultado es: ' + str(base*altura/2)

import doctest
doctest.testmod()
