from tkinter import *
raiz=Tk()
raiz.title("Ventana Mantenimiento")
raiz.iconbitmap("icono.ico")
#raiz.geometry("500x300")
raiz.config(bg="blue")
miframe=Frame()
miframe.pack()  #Metodo que empacheta el "Frame" dentro de la raiz

'''
miframe.pack(side="right") #side=Lado --> espeficica a que lado se va a ajutar su posicion con respecto a la raiz.
miframe.pack(side="top") #side=Lado --> espeficica a que lado se va a ajutar su posicion con respecto a la raiz.
miframe.pack(side="bottom") #side=Lado --> espeficica a que lado se va a ajutar su posicion con respecto a la raiz.
miframe.pack(side="left") #side=Lado --> espeficica a que lado se va a ajutar su posicion con respecto a la raiz.
miframe.pack(side="left", anchor="e") #Maneja puntos cardinales (n, e, w, s)
'''

'''
miframe.pack(fill="x")                    #Reimenciona en forma horizontal
miframe.pack(fill="y", expand="True")     #Reimenciona en forma verticalmente
miframe.pack(fill="both", expand="True")  #Reimenciona en forma vertical y horizontal
'''

miframe.config(bg="red")
miframe.config(width="250", height="150")

miframe.config(bd=10)   #Establece grosor del borde (por defecto es 0)
miframe.config(relief="sunken")
miframe.config(cursor="hand2")
raiz.mainloop()
