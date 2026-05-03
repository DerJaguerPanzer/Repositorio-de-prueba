from tkinter import END, messagebox, ttk
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("220x400")
ventana.title("Calculadora")

ttk.Label(ventana,text="INGRESAR VALOR 1").place(x=20,y=40)
txValor1 = ttk.Entry(ventana)
txValor1.place(x=20,y=80)

ttk.Label(ventana,text="INGRESAR VALOR 2").place(x=20,y=120)
txValor2 = ttk.Entry(ventana)
txValor2.place(x=20,y=160)

ttk.Label(ventana,text="Selecciona una operación:").place(x=20,y=200)
cbOperaciones = ttk.Combobox(ventana, state="readonly", values=["Sumar","Restar","Multiplicar","Dividir"])
cbOperaciones.place(x=20,y=240)


def operacion():
    
    opcion = cbOperaciones.get()
    Valor1 = float(txValor1.get())
    Valor2 = float(txValor2.get())
    
    if opcion == "Sumar":
        resultado = Valor1 + Valor2 
    elif opcion == "Restar ":
        resultado = Valor1 - Valor2
    elif opcion == "Multiplicar":
        resultado = Valor1 * Valor2
    elif opcion == "Dividir":
        resultado = Valor1 / Valor2
    else:
        messagebox.showerror(message="Por favor, selecciona una operación")
    
    txResultado.config(state="normal") 
    txResultado.delete(0, END) 
    txResultado.insert(0, str(resultado)) 
    txResultado.config(state="readonly")
    
ttk.Label(ventana, text="Resultado:").place(x =20, y = 280)
txResultado = tk.Entry(ventana, width=25, state="readonly") # caja de texto para mostrar el resultado, con estado de solo lectura
txResultado.place(x =20, y = 320)

def limpiar():
    cbOperaciones.config(state="normal")
    txResultado.config(state="normal")
    cbOperaciones.set("")
    txValor1.delete(0,END) 
    txValor2.delete(0,END)
    txResultado.delete(0,END) 
    cbOperaciones.config(state="readonly")
    txValor1.focus()

ttk.Button(ventana, text="Aceptar", command=operacion).place(x=20,y=360)

ttk.Button(ventana, text="Limpiar", command=lambda:limpiar()).place(x=120,y=360)

ventana.mainloop()