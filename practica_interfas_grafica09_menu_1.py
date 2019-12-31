from tkinter import *
from tkinter import messagebox
window=Tk()

def acerca_de():
    messagebox.showinfo("Informacion", "Sistemas Facturacion v 1.3")
def aviso_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia.")
def salirAplicacion():
    respuesta=messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")
    if respuesta==True:
        window.destroy()
    '''
    respuesta=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if respuesta=="yes":
        window.destroy()
    '''
def cerrarDocumento():
    respuesta=messagebox.askretrycancel("Reintentar","NO es posible cerrar.\nDocumento esta Bloqueado")
    if respuesta==False:
        window.destroy()

barraMenu=Menu(window)
window.config(menu=barraMenu)
archivoMenu=Menu(barraMenu)
archivoEdicion=Menu(barraMenu)
archivoAyuda=Menu(barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_cascade(label="Nuevo")
archivoMenu.add_cascade(label="Guardar")
archivoMenu.add_cascade(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_cascade(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_cascade(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_cascade(label="Copiar")
archivoEdicion.add_cascade(label="Cortar")
archivoEdicion.add_cascade(label="Pegar")

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_cascade(label="Licencia", command=aviso_licencia)
archivoAyuda.add_cascade(label="Acerca de...", command=acerca_de)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Archivo", menu=archivoEdicion)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
window.mainloop()
