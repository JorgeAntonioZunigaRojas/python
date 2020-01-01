import re
nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="sandra López"
nombre4="Jara López"
nombre5="Lara López"
nombre6="25 Antonio"

#match
#--> La funcion match solo busca desde el inicio de la cadena...

print("--> Busca una cadena dentro de otra y distinge entre mayuscula y minusculas")
if re.match("Sandra", nombre3):
    print("Hemos encontrado el nombre")
else:
    print("NO hemos encontrado el nombre")

print("--> Busca una cadena dentro de otra e IGNORA entre mayuscula y minusculas")
if re.match("Sandra", nombre3, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("NO hemos encontrado el nombre")

print("--> valida que la cadena inicie con cualquier letra pero que las siguientes sea [ara]")
if re.match(".ara", nombre4, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("NO hemos encontrado el nombre")

print("--> Inicia con un Numero")
if re.match("\d", nombre6):
    print("Hemos encontrado")
else:
    print("NO hemos encontrado")

#-->re.search() Busca en todo la cadena de caracteres usuado preferentemente en cadenas de texto muy grandesssss
print("USANDO LA FUNCION <<<search>>>")
codigo="Hola q tal como esta espero no del todo mal aun .."
if re.search("espero", codigo):
    print("Encontrado")
else:
    print("NO Encontrado")
