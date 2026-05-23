from tkinter import messagebox, ttk, END
import tkinter as tk

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("600x300")


# Etiqueta para seleccionar el tipo de conversion
tk.Label(ventana, text = "Seleccione un tipo de conversion" ).place(x=20,y=20)

selector =tk.IntVar()
texto_etiqueta1=""
texto_etiqueta2=""

#Botones de Radio 
celcius_kelvin = tk.Radiobutton(ventana,text= "Celcius - Kelvin",variable = selector, value=1,command=lambda: selector_etiquetas(Etiqueta1, Etiqueta2))
celcius_kelvin.place(x=20, y=40)
celcius_fahrenheit = tk.Radiobutton(ventana, text= "Celcius - Fahrenheit",variable = selector,value=2,command=lambda: selector_etiquetas(Etiqueta1, Etiqueta2))
celcius_fahrenheit.place(x=20, y=60)
kelvin_celsius = tk.Radiobutton(ventana, text ="Kelvin - Celsius", variable = selector, value=3, command=lambda: selector_etiquetas(Etiqueta1, Etiqueta2))
kelvin_celsius.place(x=20, y=80)
fahrenheit_celsius = tk.Radiobutton(ventana, text = "Fahrenheit - Celsius",variable = selector, value=4, command=lambda: selector_etiquetas(Etiqueta1, Etiqueta2))
fahrenheit_celsius.place(x=20, y =100)

Etiqueta1 = tk.Label(ventana, text = texto_etiqueta1)
Etiqueta2 = tk.Label(ventana, text = texto_etiqueta2)
Etiqueta1.place(x=300, y=20)
Etiqueta2.place(x=300, y=120)

def selector_etiquetas(Etiqueta1, Etiqueta2):
    global texto_etiqueta1, texto_etiqueta2

    if selector.get() == 1:
        texto_etiqueta1 = "Ingrese los grados celsius a convertir:"
        texto_etiqueta2 = "Kelvin:"
    elif selector.get() == 2:
        texto_etiqueta1 = "Ingrese los grados celsius a convertir:"
        texto_etiqueta2 = "Fahrenheit:"
    elif selector.get() == 3:
        texto_etiqueta1 = "Ingrese los grados kelvin a convertir:"
        texto_etiqueta2 = "Celsius:"
    elif selector.get() == 4:
        texto_etiqueta1 = "Ingrese los grados fahrenheit a convertir"
        texto_etiqueta2 = "Celsius"
    Etiqueta1.config(text= texto_etiqueta1)
    Etiqueta2.config(text= texto_etiqueta2)

Entrada1 = tk.Entry(ventana,state="normal")
Entrada1.place(x=300,y=40)
Entrada2 = tk.Entry(ventana,state = "readonly")
Entrada2.place(x=300,y=140)

def conversor_temperatura():
    try:
        grados= 0
        grados = float(Entrada1.get())

        Entrada2.config(state = "normal")

        if selector.get() == 1:
            conversion = grados + 273.15
        elif selector.get() == 2:
            conversion = (grados * 9/5) + 32
        elif selector.get() == 3:
            conversion = grados -273.15
        elif selector.get() == 4:
            conversion = (grados-32) * 5/9

        Entrada2.insert(0,float(conversion))
        Entrada2.config(state = "readonly")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número.")

def limpiar_entradas():
    Entrada1.delete(0, END)
    Entrada2.config(state = "normal")
    Entrada2.delete(0, END)
    Entrada2.config(state = "readonly")

tk.Button(ventana,text="Resultado",command = conversor_temperatura).place(x=300,y=80)
tk.Button(ventana,text="Limpiar",command = limpiar_entradas).place(x=400,y=80)

ventana.mainloop()


