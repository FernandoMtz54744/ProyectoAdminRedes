import tkinter as tk

from tkinter import *

from tkinter import ttk

from tkinter import messagebox

from proyecto import *



#Funciones

def mostrarTexto(texto):

    outputtext.delete('1.0', END)

    outputtext.insert(INSERT,texto)



#Configuracion de la ventana

ventana = Tk()

ventana.title("Practica Final")

ventana.geometry("1500x800")

ventana["bg"] = "#242424"



titulo = Label(text="Administracion de Servicios en Red\nPractica Final\n Cortes Lopez Jaime Alejandro / Martinez Martinez Fernando", bg="#242424", font=("Arial", 16), fg="#ffffff")

titulo.place(x=550,y=2)



confRouterButton = Button( text='Configuracion Routers', bg="#26c6da" , command=lambda: mostrarTexto(confRouter()), width=20, height=2)

confRouterButton.place(x=20, y=100)



confVPCButton = Button( text='Configuracion VPCs', bg="#26c6da" , command=lambda: mostrarTexto("VPC Config"), width=20, height=2)

confVPCButton.place(x=20, y=150)



confACLButton = Button( text='Configuracion ACL', bg="#26c6da" , command=lambda: mostrarTexto(confACL()), width=20, height=2)

confACLButton.place(x=20, y=200)



confNATButton = Button( text='Configuracion NAT', bg="#26c6da" , command=lambda: mostrarTexto(confNAT()), width=20, height=2)

confNATButton.place(x=20, y=250)



confEnrutButton = Button( text='Mostrar enrutamiento', bg="#26c6da" , command=lambda: mostrarTexto(confEnrut()), width=20, height=2)

confEnrutButton.place(x=20, y=300)



outputtext = Text(height=35, width=150)

outputtext.grid(column=1, row=5)

outputtext.place(x=250, y=100)



ventana.mainloop()