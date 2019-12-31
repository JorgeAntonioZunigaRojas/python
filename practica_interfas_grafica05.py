from tkinter import *

raiz = Tk()
raiz.title("Ventana de Practicas")
miframe = Frame(raiz, width=1200, height=600)
miframe.pack()
minombre=StringVar()
cuadroNombre = Entry(miframe, textvariable=minombre)
cuadroApellido = Entry(miframe)
cuadroDireccion = Entry(miframe)
cuadroContraseña = Entry(miframe)
textoComentario = Text(miframe, width=15, height=5)

scrollVertical= Scrollbar(miframe, command=textoComentario.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew") #--> sticky="nsew" --> establece el alto de la barra de despazamiento vertical deacuerdo al alto del textcomentario

textoComentario.config(yscrollcommand=scrollVertical.set)   #--> Establece en el objeto "textoComentario" la barra de desplaza,iento a usar

labelNombre = Label(miframe, text="Nombre: ")
labelApellido = Label(miframe, text="Apellido: ")
labelDireccion = Label(miframe, text="Direccion de hogar: ")
labelContraseña = Label(miframe, text="Contraseña: ")
labelComentario = Label(miframe, text="Comentario: ")

cuadroNombre.grid(row=0, column=1, padx=2, pady=2)
cuadroApellido.grid(row=1, column=1, padx=2, pady=2)
cuadroDireccion.grid(row=2, column=1, padx=2, pady=2)
cuadroContraseña.grid(row=3, column=1, padx=2, pady=2)
textoComentario.grid(row=4, column=1, padx=2, pady=2)

cuadroContraseña.config(show="*")

cuadroNombre.config(fg="red", justify="right")
cuadroApellido.config(fg="blue", justify="center")
labelDireccion.config(fg="black", justify="left")
labelContraseña.config(fg="black", justify="left")
labelComentario.config(fg="black", justify="left")

labelNombre.grid(row=0, column=0, sticky="e", padx=2,
                 pady=2)  # Alineacion al este=derecha=(sticky="e"), Distancia entre objetos=(padx=10)
labelApellido.grid(row=1, column=0, sticky="e", padx=2, pady=2)
labelDireccion.grid(row=2, column=0, sticky="e", padx=2, pady=2)
labelContraseña.grid(row=3, column=0, sticky="e", padx=2, pady=2)
labelComentario.grid(row=4, column=0, sticky="e", padx=2, pady=2)

def funcionCodigoBoton():
    minombre.set("Toño")

botonEnviar=Button(raiz, text="Enviar", command=funcionCodigoBoton)
botonEnviar.pack()

raiz.mainloop()
