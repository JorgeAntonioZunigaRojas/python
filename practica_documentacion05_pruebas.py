#--> este archivo muestra como realizar pruebas con multiples lineas de codigo de la documentacion
import math
def raizcuadrada(listaNumeros):
    """
    La funcion devuelve una lista con la raiz cuadrada de los elementos numericos pasados por parametros en otra lista

    >>> lista=[]
    >>> for i in [4,9,19]:
    ...     lista.append(i)
    >>> raizcuadrada(lista)
    [2.0, 3.0, 4.0]
    """
    return [math.sqrt(n) for n in listaNumeros]

import doctest
doctest.testmod()