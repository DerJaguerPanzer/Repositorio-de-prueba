import tkinter as tk
from tkinter import messagebox, ttk, END

ventana=tk.Tk()
ventana.config(width=300,height=300)
ventana.title("Calculadora POO")

class Calculadora():

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        return self.n1 + self.n2
    
tk.Label(ventana, text="Ingrese el primer numero").place(x=20, y=20)
Entrada1 = tk.Entry(ventana)
Entrada1.place(x=20, y=40)
tk.Label(ventana, text="Ingrese el segundo numero").place(x=20, y=80)
Entrada2 = tk.Entry(ventana)
Entrada2.place(x=20, y=100)
def calcular():
    try:
        num1 = float(Entrada1.get())
        num2 = float(Entrada2.get())
        calculadora = Calculadora(num1, num2)
        resultado = calculadora.suma()
        messagebox.showinfo(message=f"El resultado de la suma es: {resultado}")
    except ValueError:
        messagebox.showerror(message="Por favor ingrese valores numéricos válidos")
        
tk.Button(ventana, text="Calcular", command=calcular).place(x=20, y=140)
ventana.mainloop()