#Funcion Filter
#-->Verificar que elementos de una secuencia cumplen una condiccion devolviendo un interador con los elementos que cumplen dicha condicion
def numero_par(numero):
    if numero%2==0:
        return  True
numeros=[17,24,7,39,8,51,92]
print(list(filter(numero_par,numeros)))

