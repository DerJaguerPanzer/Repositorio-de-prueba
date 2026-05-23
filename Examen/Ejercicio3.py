import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title("Bisiesto")
ventana.geometry("300x250")

tk.Label(ventana, text="Revisa si un año es bisiesto").pack(pady=10)
tk.Label(ventana, text="Ingrese un año:").pack(pady=5)
entrada_año = tk.Entry(ventana)
entrada_año.pack(pady=5)

class Biciesto:
    def __init__(self, year):
        self.year = year

    def es_biciesto(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        else:
            return False

def comprobar_año():
    try:
        año_ingresado = int(entrada_año.get()) 
        
        validador = Biciesto(año_ingresado)
        
        if validador.es_biciesto():
            messagebox.showinfo("Resultado", f"El año {año_ingresado} SÍ es bisiesto.")
        else:
            messagebox.showinfo("Resultado", f"El año {año_ingresado} NO es bisiesto.")
            
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número de año válido.")

boton_comprobar = ttk.Button(ventana, text="Verificar", command=comprobar_año)
boton_comprobar.pack(pady=15)

ventana.mainloop()