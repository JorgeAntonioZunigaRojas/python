from tkinter import *
from tkinter import filedialog
root=Tk()

root.config(width=300, height=500)

def abrirFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de excel","*.xlsx"),("Ficheros de texto","*.docx"),("Todos los ficheros","*.*")))
    print(fichero)

Button(root, text="Abrir Fichero", command=abrirFichero).pack()
root.mainloop()

