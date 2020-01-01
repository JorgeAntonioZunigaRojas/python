#-->lambda
#---->"lambda" permite elaborar funciones simples en una sola linea
#Funcion Filter
#-->Verificar que elementos de una secuencia cumplen una condiccion devolviendo un interador con los elementos que cumplen dicha condicion
numeros=[17,24,7,39,8,51,93]
validar_numero_par=lambda numero: numero%2==0
print(list(filter(validar_numero_par,numeros)))

