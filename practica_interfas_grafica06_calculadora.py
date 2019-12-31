from tkinter import *
window=Tk()
container=Frame(window)
container.pack()
#--> SCREEN <--------------------------------------------------------
numberScreen=StringVar()
screen=Entry(container, textvariable=numberScreen)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(bg="black", fg="#03f943", justify="right")

#--> Functions 1 <--------------------------------------------------------
def numeroPulsado(numero):
    numberScreen.set(numberScreen.get() + numero)
#--> BOTONES 1 <--------------------------------------------------------
boton7=Button(container, text="7", width=3, command=lambda:numeroPulsado("7"))
boton8=Button(container, text="8", width=3, command=lambda:numeroPulsado("8"))
boton9=Button(container, text="9", width=3, command=lambda:numeroPulsado("9"))
botonD=Button(container, text="/", width=3, command=lambda:numeroPulsado(""))

boton4=Button(container, text="4", width=3, command=lambda:numeroPulsado("4"))
boton5=Button(container, text="5", width=3, command=lambda:numeroPulsado("5"))
boton6=Button(container, text="6", width=3, command=lambda:numeroPulsado("6"))
botonM=Button(container, text="x", width=3, command=lambda:numeroPulsado(""))

boton1=Button(container, text="1", width=3, command=lambda:numeroPulsado("1"))
boton2=Button(container, text="2", width=3, command=lambda:numeroPulsado("2"))
boton3=Button(container, text="3", width=3, command=lambda:numeroPulsado("3"))
botonR=Button(container, text="-", width=3, command=lambda:numeroPulsado(""))

boton0=Button(container, text="0", width=3, command=lambda:numeroPulsado("0"))
botonP=Button(container, text=".", width=3, command=lambda:numeroPulsado("."))
botonI=Button(container, text="=", width=3, command=lambda:numeroPulsado(""))
botonA=Button(container, text="+", width=3, command=lambda:numeroPulsado(""))

boton7.grid(row=2, column=1)
boton8.grid(row=2, column=2)
boton9.grid(row=2, column=3)
botonD.grid(row=2, column=4)

boton4.grid(row=3, column=1)
boton5.grid(row=3, column=2)
boton6.grid(row=3, column=3)
botonM.grid(row=3, column=4)

boton1.grid(row=4, column=1)
boton2.grid(row=4, column=2)
boton3.grid(row=4, column=3)
botonR.grid(row=4, column=4)

boton0.grid(row=5, column=1)
botonP.grid(row=5, column=2)
botonI.grid(row=5, column=3)
botonA.grid(row=5, column=4)


window.mainloop()


