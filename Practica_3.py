# Importar las librerias para generar ventanas y sus objetos

from tkinter import END, messagebox, ttk
import tkinter as tk

#Crear la ventana

ventana = tk.Tk() #Esta linea crea la ventana
ventana.config(width=235,height=200) #Configura el tamaño de la ventana
ventana.title("Practica 3") #Configura el titulo de la ventana


#Crea una etiqueta para pedir el precio al usuario
ttk.Label(ventana, text="Ingrese el precio:").place(x =20, y = 30) 

#Entry nos sirve para crear cajas
txPrecio = ttk.Entry(ventana)
txPrecio.place(x =20, y = 50)

txResultado = tk.Entry(ventana)
txResultado.place(x =20, y = 80)

def aumentaPorcentaje():
    precio = 0.0
    resultado = 0.0 
    precio = float(txPrecio.get())
    resultado = precio*1.16 # aumenta el iva o el 16%

    txResultado.delete(0, END) # limpia el resultado anterior
    txResultado.insert(0,f"{resultado:.2f}") # muestra el resultado en la caja de texto

btCalcular = ttk.Button(ventana, width=10, text="Calcular", command=aumentaPorcentaje) # , comand = aumentaPorcentaje
btCalcular.place(x =20, y = 110)

ventana.mainloop() #Esta linea hace que la ventana se mantenga abierta
