from io import open

'''
# Abrir archivo modo escritura  #################################################################
name_file="archivo.txt"
modo_apertura="w"  # (r=(lectura), w=(escritura), a=(modificar un archivo existente)  )
archivo_texto=open(name_file, modo_apertura)    #Si el archivo no existe esta linea de codigo lo CREA
linea="Primera linea del archivo"
archivo_texto.write(linea)
archivo_texto.close()
'''

'''
# Abrir archivo modo lectura (almacena lo leido en una variable de texto #######################
name_file="archivo.txt"
modo_apertura="r"  # (r=(lectura), w=(escritura), a=(modificar un archivo existente)  )
archivo_texto=open(name_file, modo_apertura)
contenido=archivo_texto.read() #Almacena todo el contenido del archivo en una variable de texto
archivo_texto.close()
print(contenido)
'''

'''
# Abrir archivo modo lectura (almacena lo leido en una variable lista #######################
name_file="archivo.txt"
modo_apertura="r"  # (r=(lectura), w=(escritura), a=(modificar un archivo existente)  )
archivo_texto=open(name_file, modo_apertura)
contenido=archivo_texto.readlines() #Almacena todo el contenido del archivo en una variable lista
archivo_texto.close()
print(contenido[0])
print(contenido[1])
'''

# Abrir archivo para modificarlo #############################################################
name_file="archivo.txt"
modo_apertura="a"  # (r=(lectura), w=(escritura), a=(modificar un archivo existente)  )
archivo_texto=open(name_file, modo_apertura)
archivo_texto.write("\nOtra linea mas al archivooo...!!!")
archivo_texto.close()


