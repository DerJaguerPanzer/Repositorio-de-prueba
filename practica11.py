from tkinter import END, messagebox, ttk
import tkinter as tk

ventana  =  tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Practica 11")

listaDatos=tk.Listbox(ventana,width=30)
listaDatos.place(x=20, y=20)

#Entry y etiqueta de promedio 
tk.Label(ventana, text= "Promedio General").place(x=220, y=20)
Promedio = tk.Entry(ventana, width=20, state= "readonly")
Promedio.place(x=220, y=40)

#Entry y etiqueta de reporbados 
tk.Label(ventana, text= "Numero de reprobados").place(x=220, y=60)
Reprobados = tk.Entry(ventana, width=20, state= "readonly")
Reprobados.place(x=220, y=80)

#Entry y etiqueta de nota maxima    
tk.Label(ventana, text= "Nota Maxima").place(x=220, y = 100)
Maxima = tk.Entry(ventana, width=20, state= "readonly")
Maxima.place(x=220, y=120)

#Funciones 
#Funcion modal crea una ventana adicional 
def modal():
    #Configuracion de la ventana modal
    modal = tk.Toplevel(ventana)
    modal.title("Añade un Valor")
    modal.geometry("150x300")
    modal.grab_set() # Bloquea la ventana principal hasta que se cierre la modal
    
    #Elementos de la ventana modal
    ttk.Label(modal, text="Introduce el nombre").pack(pady=5)
    entrada_nombre = ttk.Entry(modal)
    entrada_nombre.pack(pady=5)
    
    ttk.Label(modal, text="Introduce la calificacion").pack(pady=5)
    entrada_calificacion = ttk.Entry(modal)
    entrada_calificacion.pack(pady=5)
    
     #Listas para almacenar los datos de la modal
    global lista_calificaciones
    lista_nombres = []
    lista_calificaciones = []

    
    #Funcion para insertar los datos de las entradas en modal a las listas correspondientes
    def insertar_datos():
        nombre = str(entrada_nombre.get())
        calificacion = float(entrada_calificacion.get())
        lista_nombres.append(nombre)
        lista_calificaciones.append(calificacion)
        agregar_listbox()
        
    def agregar_listbox():
        listaDatos.delete(0,END)
        for i in range(len(lista_nombres)):
            listaDatos.insert(i, f"{lista_nombres[i]}, {lista_calificaciones[i]}")
        entrada_calificacion.delete(0,END)
        entrada_nombre.delete(0,END)
        entrada_nombre.focus()

        #Promedio General
        Promedio.config(state="normal") 
        Promedio.delete(0, END) 
        #Logica
        sumatoria = sum(lista_calificaciones)
        promedio_general = sumatoria / len(lista_calificaciones)

        Promedio.insert(0, str(promedio_general)) 
        Promedio.config(state="readonly")

        #Nota Maxima
        Maxima.config(state ="normal")
        Maxima.delete(0,END)
        #Logica
        nota_maxima = max(lista_calificaciones)

        Maxima.insert(0, str(nota_maxima))
        Maxima.config(state = "readonly")

        #Reprobados
        Reprobados.config(state ="normal")
        Reprobados.delete(0, END)

        #Logica
        cantidad_reprobados = 0
        for i in range(len(lista_calificaciones)):
            if lista_calificaciones[i] < 60:
                cantidad_reprobados += 1
            elif i == len(lista_calificaciones):
                break 
            i+=1    

        Reprobados.insert(0, str(cantidad_reprobados))
        Reprobados.config(state="readonly")
    
    ttk.Button(modal, text="Agregar a la lista", command=insertar_datos).pack(pady=5)

       
#Botones

ttk.Button(ventana, text= "Nuevo Alumno", command=modal).place(x=220, y=150)

ventana.mainloop()