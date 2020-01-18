from flask import Flask
from flask_mysqldb import MySQL


'''
for i in ["Peru", "Ecuador", "Chile", "Bolivia", "Brasil"]:
    print(i)
'''
'''
for i in ["Peru", "Ecuador", "Chile", "Bolivia", "Brasil"]:
    # la palabra reservada "end" por defecto almacena un salto de linea. Es por ello que las impresiones van una debajo de otra
    # si desearamos modificar el valor de "end" hacer lo siguiente:
    print(i, end=" - ")
'''
'''
print(range(4))
for i in range(4):
    print(i)
'''
'''
for letra in "Python":
    print("Letra: {}".format(letra))
'''
'''
email=""
for i in email:
    print(i)
    if i=="@":
        print("Esto es un arroba: {}".format(i))
        break;
else:   #Este el el "else" del bucle "for" y se ejecuta siempre en cuando el bucle for no se ejecute (no se ejecute por que este vacio.)
    print("se imprimira si el bucle esta vacio")
'''

email='jorgezuñigarojas1@gmail.com'
for i in email:
    print('antes del if: {}'.format(i))
    if i=="@":
        print("Esto es un arroba: {}".format(i))
        break;  #Rope el bucle repetitivo...........
    print('despues del if: {}'.format(i))
