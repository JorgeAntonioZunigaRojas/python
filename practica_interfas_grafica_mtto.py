from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=400, height=500)

menuBD=Menu(barraMenu, tearoff=0)
menuBD.add_command(label="Conectar")
menuBD.add_command(label="salir")

menuBorrar=Menu(barraMenu, tearoff=0)
menuBorrar.add_command(label="Borrar campos")

menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label="Crear")
menuCRUD.add_command(label="Leer")
menuCRUD.add_command(label="Actualizar")
menuCRUD.add_command(label="Borrar")

menuAyuda=Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Licencia")
menuAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD",menu=menuBD)
barraMenu.add_cascade(label="Borrar",menu=menuBorrar)
barraMenu.add_cascade(label="CRUD",menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)

#--> Campos >---------------------------------------------------------------------------
miframe=Frame(root)
miframe.pack()

cuadroID=Entry(miframe)
cuadroID.grid(row=0, column=1, padx=10, pady=2)

cuadroNombre=Entry(miframe)
cuadroNombre.grid(row=1, column=1, padx=10, pady=2)

cuadroPass=Entry(miframe)
cuadroPass.grid(row=2, column=1, padx=10, pady=2)
cuadroPass.config(show="*")

cuadroApellido=Entry(miframe)
cuadroApellido.grid(row=3, column=1, padx=10, pady=2)

cuadroDireccion=Entry(miframe)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=2)

cuadroComentario=Entry(miframe)
cuadroComentario=Text(miframe, width=16, height=5)
cuadroComentario.grid(row=5, column=1, padx=10, pady=2)
scrollVert=Scrollbar(miframe, command=cuadroComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollVert.set)


root.mainloop()