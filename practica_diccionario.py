#pais_capital={"Peru":"Lima", "Chile": "Santiago", "Argentina":"Buenos Aires", "Colimbia": "Bogota"}
#print(pais_capital)         #imprime todo el diccionario
#print(pais_capital["Peru"]) #Imprime la capital (Valor de la clave Peru)

#midiccionario={43809897: "Jorge Antonio Zuñiga Rojas", "Peru": "Lima", "Docena":12}
#print(midiccionario[43809897])
#print(midiccionario["Docena"])
#print(midiccionario["Peru"])

#midiccionario={23:"Jorge", "Toño": "Programador", "Años Campeon": [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011]} #Una lista dentro de un diccionario
#print(midiccionario)
#print(midiccionario["Años Campeon"])

midiccionario={23:"Jorge", "Toño": "Programador", "Años Campeon": {"Temporadas": [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011]}} #un diccioario dentro de otro diccionario
print(midiccionario)
print(midiccionario["Años Campeon"])


print(midiccionario.keys())     #Imprime las clave del diccionario
print(midiccionario.values())   #Imprime los valores del diccionario

