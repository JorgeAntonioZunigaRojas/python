from tkinter import *
ventana=Tk()
varOpcion1=StringVar()

def imprimir_genero_elegido():
    etiqueta.config(text="Genero Elejido {}".format(varOpcion1.get()))

varOpcion1.set("Masculino") #Valor por defecto
Radiobutton(ventana, text="Masculino", variable=varOpcion1, value="Masculino", command=imprimir_genero_elegido).pack()
Radiobutton(ventana, text="Femenino", variable=varOpcion1, value="Femenino", command=imprimir_genero_elegido).pack()

etiqueta=Label(ventana, text="Genero Elejido {}".format(varOpcion1.get()))
etiqueta.pack()
ventana.mainloop()
