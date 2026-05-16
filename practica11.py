from tkinter import END, messagebox, ttk
import tkinter as tk

ventana  =  tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Practica 11")

listaDatos=tk.Listbox(ventana,width=30)
listaDatos.place(x=20, y=20)

#Entry y etiqueta de promedio 
tk.Label(ventana, text= "Promedio General").place(x=220, y=20)
Promeido = tk.Entry(ventana, width=20)
Promeido.place(x=220, y=40)

#Entry y etiqueta de reporbados 
tk.Label(ventana, text= "Numero de resultados").place(x=220, y=60)
Reprobados = tk.Entry(ventana, width=20)
Reprobados.place(x=220, y=80)

#Entry y etiqueta de nota maxima    
tk.Label(ventana, text= "Nota Maxima").place(x=220, y = 100)
Maxima = tk.Entry(ventana, width=20)
Maxima.place(x=220, y=120)

#Funciones 

def modal():
    modal = tk.Toplevel(ventana)
    modal.title("Añade un Valor")
    modal.grab_set() 
    
    ttk.Label(modal, text="Introduce un numero a añadir").pack(pady=5)
    entrada_modal = ttk.Entry(modal)
    entrada_modal.pack(pady=5)

def agregar():
    pass 


#Botones

ttk.Button(ventana, text= "Nuevo Alumno", command=modal).place(x=220, y=150)


ventana.mainloop()