# Seriaslizar objetos
import pickle
class vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera = False
        self.frena = False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print("Marca ",self.marca, "\nModelo: ", self.modelo,"\nEn Marcha: ",self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando: ",self.frena)

coche1=vehiculo("Akme", "XYZ")
coche2=vehiculo("Seat", "Leon")
coche3=vehiculo("Renault", "Megane")
coches=[coche1, coche2, coche3]
fichero=open("archivo_binario_loscoches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del (fichero)

fichero_apertura=open("archivo_binario_loscoches", "rb")    #--> rb=lectura binarios
miscoches=pickle.load(fichero_apertura)
fichero_apertura.close()
for i in miscoches:
    print(i.estado())
