import pickle
'''
# Guardar una lista en un fichero binario
lista_nombres=["Pedro", "Ana","Juan","Maria","Isabel"]
fichero_binario=open("archivo_binario_lista_nombres","wb")   #--> wb=Escritura binaria
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()
del (fichero_binario)   # Elimina el "fichero_binario" de la memoria.
'''

# Leer un fichero binario
fichero_binario=open("archivo_binario_lista_nombres","rb")   #--> rb=leer archivo binario
lista=pickle.load(fichero_binario)
print(lista)
