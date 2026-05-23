from tkinter import END, messagebox, ttk
import tkinter as tk

Ventana = tk.Tk()
Ventana.config(width=400,height=400)
Ventana.title("Minimo y Maximo")

ttk.Label(Ventana,text="Ingresa el valor 1").place(x=20,y=20)
entry_1 =ttk.Entry(Ventana)
entry_1.place(x=20,y=60)


ttk.Label(Ventana,text="Ingresa el valor 2").place(x=20,y=100)
entry_2 = ttk.Entry(Ventana)
entry_2.place(x=20,y=140)

ttk.Label(Ventana,text="Ingresa el valor 3").place(x=20,y=180)
entry_3 = ttk.Entry(Ventana)
entry_3.place(x=20,y=220)


ttk.Label(Ventana,text="Resultado").place(x=20,y=260) 
Resultado = tk.Entry(Ventana, width=25, state= "readonly")
Resultado.place(x=20,y=300)


# def Maximo():
    
#     Resultado.config(state="normal")

#     num1 = float(entry_1.get())
#     num2 = float(entry_2.get())
#     num3 = float(entry_3.get())
#     resultado = max(num1,num2,num3)
#     Resultado.delete(0, END)
#     Resultado.insert(0, resultado)
#     Resultado.config(state="readonly")
    


# def Minimo():
#     Resultado.config(state="normal")

#     num1 = float(entry_1.get())
#     num2 = float(entry_2.get())
#     num3 = float(entry_3.get())
#     resultado = min(num1,num2,num3)
#     Resultado.delete(0, END)
#     Resultado.insert(0, resultado)
#     Resultado.config(state="readonly")


def Maximo():
    
    Resultado.config(state="normal")

    num1 = float(entry_1.get())
    num2 = float(entry_2.get())
    num3 = float(entry_3.get())
    if num1 > num2 and num1 > num3:
        resultado = num1
    elif num2 > num1 and num2 > num3:
        resultado = num2
    else:
        resultado = num3

    Resultado.delete(0, END)
    Resultado.insert(0, resultado)
    Resultado.config(state="readonly")
    

def Minimo():
    Resultado.config(state="normal")

    num1 = float(entry_1.get())
    num2 = float(entry_2.get())
    num3 = float(entry_3.get())
    if num1 < num2 and num1 < num3:
        resultado = num1
    elif num2 < num1 and num2 < num3:
        resultado = num2
    else:
        resultado = num3
    
    Resultado.delete(0, END)
    Resultado.insert(0, resultado)
    Resultado.config(state="readonly")

def Limpiar():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)   
    Resultado.config(state="normal")
    Resultado.delete(0, END)
    Resultado.config(state="readonly") 

ttk.Button(Ventana, width=5, text = " Maximo", command= Maximo).place(x= 20,y=340)
ttk.Button(Ventana, width=10, text = " Minimo", command= Minimo).place(x= 120,y=340)
ttk.Button(Ventana, width=10, text = " Limpiar",command= Limpiar).place(x= 220,y=340)

Ventana.mainloop()

