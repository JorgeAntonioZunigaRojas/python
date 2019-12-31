from tkinter import *
ventana=Tk()
varOpcion1=IntVar()
varOpcion1.set(0)
def imprimir_genero_elegido():
    if varOpcion1.get()==1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

Radiobutton(ventana, text="Masculino", variable=varOpcion1, value=1, command=imprimir_genero_elegido).pack()
Radiobutton(ventana, text="Femenino", variable=varOpcion1, value=2, command=imprimir_genero_elegido).pack()

etiqueta=Label(ventana, text="Genero Elejido?")
etiqueta.pack()
ventana.mainloop()
