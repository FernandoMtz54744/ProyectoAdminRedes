import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from proyecto import *

#Funcion para mostrar el texto en interfaz
def mostrarTexto(texto):
    outputtext.delete('1.0', END) #Se borra el texto existente
    outputtext.insert(INSERT,texto) #Se agrega el nuevo texto

#Configuracion de la ventana
ventana = Tk()
ventana.title("Practica Final") #Titulo de ventana
ventana.geometry("1000x500") #Tamanio de ventana
ventana["bg"] = "#242424" #Color de fondo

#Etiqueta con el titulo
titulo = Label(text="Administracion de Servicios en Red\nPractica Final\n Cortes Lopez Jaime Alejandro / Martinez Martinez Fernando",
bg="#242424", font=("Arial", 16), fg="#ffffff")
titulo.place(x=300,y=2)

#Boton para obtener configuracion de interfaces
confRouterButton = Button( text='Configuracion Routers', bg="#26c6da", 
	command=lambda: mostrarTexto(executeCommand('show ip int brief')), width=20, height=2)
confRouterButton.place(x=20, y=100)

#Boton para obtener configuracion de ACL
confACLButton = Button( text='Configuracion ACL', bg="#26c6da", 
	command=lambda: mostrarTexto(executeCommand('show access-list')), width=20, height=2)
confACLButton.place(x=20, y=150)

#Boton para obtener configuracion de NAT
confNATButton = Button( text='Configuracion NAT', bg="#26c6da", 
	command=lambda: mostrarTexto(executeCommand('show ip nat translation')), width=20, height=2)
confNATButton.place(x=20, y=200)

#Boton para obtener configuracion de enrutamiento
confEnrutButton = Button( text='Mostrar enrutamiento', bg="#26c6da", 
	command=lambda: mostrarTexto(executeCommand('show ip rou')), width=20, height=2)
confEnrutButton.place(x=20, y=250)

#Componente para mostrar texto en la interfaz
outputtext = Text(height=20, width=90)
outputtext.grid(column=1, row=5)
outputtext.place(x=250, y=100)

#Se inicia la interfaz
ventana.mainloop()