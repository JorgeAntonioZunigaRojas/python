from tkinter import *
raiz=Tk()
raiz.title("Mantenimiento")
raiz.resizable(False,False)  #Parametros booleanos que permiten redimencionar la pantalla ancho y alto despectivamente.
raiz.geometry("500x300")
raiz.iconbitmap("icono.ico")
raiz.config(bg="blue")
raiz=mainloop()
# El metodo "mainloop" siempre debe esta al final del codigo..
# El metodo "mainloop" es un bucle infinito (que siempre esta en ejecucion) que esta a la escucha de posibles eventos que se ejecuten con la interacion entre la ventana y el usuario.



