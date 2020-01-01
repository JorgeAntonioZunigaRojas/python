#¿Que son las expresiones regulares regex?
#-->Se usan para buscar una cadena de caracteres dentro de otra cadena de caracteres.
import re
cadena="Vamos a aprender expresiones regulares"
texto_a_buscar="aprenderr"
objeto_respuesta=re.search(texto_a_buscar,cadena)
if objeto_respuesta is not None:
    print("Posicion Inicial",objeto_respuesta.start())
    print("Posicion Final",objeto_respuesta.end())
    print(objeto_respuesta.span())
    print("El texto ha sido encontrado")
else:
    print("El texto NO ha sido encontrado")

print("-------------------------------------")
print(objeto_respuesta)
print("-------------------------------------")
print(re.findall("a",cadena))   #--> retorna en una lista elementos
print(len(re.findall("a",cadena))) #--> retorna en una lista elementos