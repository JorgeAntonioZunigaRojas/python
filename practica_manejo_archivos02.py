from io import open
# Modificar contenido con una variable lista
archivo_texto=open("archivo.txt", "r+") # [r+]=Lectura y Escritura
lista=archivo_texto.readlines()
lista[0]="Comienzo del texto1\n"
lista[3]='Otra linea mas al archivooo...!!!\nFin del comienzo del texto\n'
archivo_texto.seek(0)   # Es muy importante reiniciar la posicion a "0" para reemplazar las linas, caso contrario se crearan nuevas lineas.
archivo_texto.writelines(lista)
archivo_texto.close()

'''
archivo_texto=open("archivo.txt", "r+") # [r+]=Lectura y Escritura
archivo_texto.write("Comienzo del texto2\n")
print(archivo_texto.readlines())
archivo_texto.close()
'''

'''
archivo_texto=open("archivo.txt", "r")
print(archivo_texto.read())     # Si no se espeficica un parametro el metodo "read" devuelve desde la posicion actual del cursor (posicion por defecto=0) hasta el final...
archivo_texto.seek(25)          # La palabra reservada "seek" posiciona el cursor en el numero de caracter especificado en el argumento.
print(archivo_texto.read())     # Lee el contenido desde la posicion actual del cursor hasta el final, dejando el cursor en la ultima posicion...
print(archivo_texto.read())     # Como la posicion actual del cursor esta al final del contenido la impresion no muestra nada....
archivo_texto.seek(0)           # Retorna el cursor a la posicion inicial (posicion=0)
print(archivo_texto.read(12))   # El parametro del metodo "read" epedifica la cantidad de caracteres a leer desde la posicion actual del cursor...
print(archivo_texto.read(13))   # El parametro del metodo "read" epedifica la cantidad de caracteres a leer desde la posicion actual del cursor...
archivo_texto.seek(0)
print(archivo_texto.readline())
print(archivo_texto.readline())
'''