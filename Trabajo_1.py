# Importar las librerias para generar ventanas y sus objetos

from tkinter import END, messagebox, ttk
import tkinter as tk

#Crear la ventana

ventana = tk.Tk() #Esta linea crea la ventana
ventana.config(width=235,height=400) #Configura el tamaño de la ventana
ventana.title("Practica 4") #Configura el titulo de la ventana

#Crea una etiqueta para pedir el precio al usuario
ttk.Label(ventana, text="Ingresa tu edad:").place(x =20, y = 30) 

#Entry nos sirve para crear cajas
txEdad = ttk.Entry(ventana)
txEdad.place(x =20, y = 50)

ttk.Label(ventana, text="Resultado:").place(x =20, y = 80)
txResultado = tk.Entry(ventana, width=25, state="readonly") # caja de texto para mostrar el resultado, con estado de solo lectura
txResultado.place(x =20, y = 100)

def define_rango_edad():
    edad = int(txEdad.get())

    txResultado.config(state="normal") # establece el estado de la caja de texto a normal para poder escribir en ella
    
    if edad < 18:
        resultado = "Eres menor de edad"
    elif edad < 59:
        resultado = "Eres mayor de edad"
    elif edad < 127:
        resultado = "Eres adulto mayor"
    else:
        resultado = "Edad no valida"
    
    txResultado.delete(0, END) # limpia el resultado anterior
    txResultado.insert(0, str(resultado)) # muestra el resultado en la caja de texto
    txResultado.config(state="readonly") # establece el estado de la caja de texto a solo lectura
    txEdad.focus() 
    

def limpiar():
    txResultado.config(state="normal")
    txEdad.delete(0, END) 
    txResultado.delete(0, END) 
    txResultado.config(state="readonly")
    txEdad.focus()

btCalcular = ttk.Button(ventana, width=10, text="Aceptar", command=lambda:define_rango_edad()) # , comand = aumentaPorcentaje
btCalcular.place(x =20, y = 130)

btLimpiar = ttk.Button(ventana, width=10, text="Limpiar", command=lambda:limpiar())# lamda busca la funcion limpiar y la ejecuta
btLimpiar.place(x =120, y = 130)

# Cargar imagen (PNG o GIF)
imagen = tk.PhotoImage(file="ejemplo.png")

# Mostrar en un Label
label = tk.Label(ventana, image=imagen)
label.place(x=20, y=300) # Posición de la imagen en la ventana
label.pack()

ventana.mainloop() #Esta linea hace que la ventana se mantenga abierta
