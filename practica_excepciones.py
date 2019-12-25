# Finally: Siempre se ejecuta (aya o noa aya error lo que este dentro de finally siempre se ejecuta)
def divide(numero1, numero2):
    try:
        a = int(numero1)
        b = int(numero2)
        return a / b
    except:
        print("Se produjo un error")
        return "Operacion Invalida"
    finally:
        print("Siempre se ejecutaaaaaa")
print(divide(8, 2))
#print(divide(8, 0))
#print(divide("sdfwer4234", "43frwfsdf"))


'''
# Ejercicio que permite capturar errores de forma general (no recomendable por que no identifica que error ha sicedido)
# El beneficio es que el programa no caiga
def divide(numero1, numero2):
    try:
        a = int(numero1)
        b = int(numero2)
        return a / b
    except:
        print("Se produjo un error")
        return "Operacion Invalida"
#print(divide(8, 0))
print(divide("sdfwer4234", "43frwfsdf"))
'''

'''
# Ejercicio que permite capturar diferente errores (Equivalente al anterior)
def divide(numero1, numero2):
    try:
        a = int(numero1)
        b = int(numero2)
        return a / b
    except ValueError:
        print("Los valores ingresados son incorrectos")
        return "Operacion Invalida (Valores de entrada incorrectos)"
    except ZeroDivisionError:
        print("NO seas [#@M5##@] No se puede dividir entre cero")
        return "Operacion Invalida (Motivo: divisor cero)"

#print(divide(8, 0))
print(divide("sdfwer4234", "43frwfsdf"))
'''

'''
# Ejercicio que permite capturar diferente errores (Equivalente al siguiente)
def divide(numero1, numero2):
    try:
        try:
            a = int(numero1)
            b = int(numero2)
        except ValueError:
            print("Los valores ingresados son incorrectos")
            return "Operacion Invalida (Valores de entrada incorrectos)"
        else:
            return a / b
    except ZeroDivisionError:
        print("NO seas [#@M5##@] No se puede dividir entre cero")
        return "Operacion Invalida (Motivo: divisor cero)"

#print(divide(8, 0))
print(divide("sdfwer4234", "43frwfsdf"))
'''