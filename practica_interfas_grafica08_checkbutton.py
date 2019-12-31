from tkinter import*
window=Tk()
window.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""
    if playa.get()==1:
        opcionEscogida=opcionEscogida+" Playa"
    if montana.get() == 1:
        opcionEscogida = opcionEscogida + " Montaña"
    if turismoRural.get() == 1:
        opcionEscogida = opcionEscogida + " Turismo Rural"
    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="python.gif")
Label(window,image=foto).pack()
frame=Frame(window)
frame.pack()
Label(frame, text="Elige Destinos", width=50).pack()

playa.set(0)
montana.set(0)
turismoRural.set(0)

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

window.mainloop()
