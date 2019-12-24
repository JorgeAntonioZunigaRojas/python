#Creacion de una tupla################################################################################################
#Caractaristica de una tupla-> una tupla no es modificable............................................................
#mitupla=("Juan",13,1,1995)
#print(mitupla)

#Transformacion de tuplas a listas y de listas a tuplas###############################################################
#mitupla=("Juan",13,1,1995)
#milista=list(mitupla)   #Transforma una tupla a lista
#print(milista)
#mitupla2=tuple(milista) #Transforma una lista a tupla
#print(mitupla2)

#Buscar elementos en una tupla########################################################################################
#mitupla=("Juan",13,1,1995)
#respuesta1="Juan" in mitupla    #Busca pedro y si lo encuentra devuelve "True" caso contrario "False"
#respuesta2="Pedro" in mitupla
#print(respuesta1)
#print(respuesta2)

#Numero de elementos de una tupla#####################################################################################
#mitupla=("Juan",13,1,1995)
#numero_elementos=len(mitupla)  #Devuelve el numero de elementos de una tupla
#print(numero_elementos)

#tupla Unitaria#######################################################################################################
#mitupla=("Juan",)   #tupla Unitaria
#print(len(mitupla))


#Desempaquetado de tuplas#############################################################################################
mitupla=("Juan",13,1,1995)
name, day, month, year=mitupla  #Desempaqueta los valores de una tupla y los almacena en variables de forma respectiva.
print(name)
print(day)
print(month)
print(year)
