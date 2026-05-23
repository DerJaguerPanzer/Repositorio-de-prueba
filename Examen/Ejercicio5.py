#Congruencia de zeller 
import tkinter as tk
from tkinter import messagebox, ttk, END

ventana=tk.Tk()
ventana.config(width=300,height=300)
ventana.title("Calculadora calendario")

tk.Label(ventana, text="Ingrese el año").place(x=20, y=20)
entrada_año = tk.Entry(ventana)
entrada_año.place(x=20, y=40)
entrada_año.focus()

tk.Label(ventana, text="Ingrese el mes").place(x=20, y=80)
entrada_mes = tk.Entry(ventana)
entrada_mes.place(x=20, y=100)

tk.Label(ventana, text="Ingrese el dia").place(x=20, y=140)
entrada_dia = tk.Entry(ventana)
entrada_dia.place(x=20, y=160)

tk.Label(ventana, text="Resultado").place(x=20, y=200)

Resulatado = tk.Entry(ventana, state="readonly")
Resulatado.place(x=20, y=220)

def calendario_gregoriano():
    try:
        año = int(entrada_año.get())
        mes = int(entrada_mes.get())
        dia = int(entrada_dia.get())
        Resulatado.config(state="normal")

        a = (14 - mes) // 12
        y = año - a
        m = mes + 12 * a - 2

        d = (5 + dia + y + y // 4 + (31 * m) // 12) % 7

        if d == 0:
            resultado = "Tu fecha fue un lunes"
        elif d == 1:
            resultado = "Tu fecha fue un martes"
        elif d == 2:
            resultado = "Tu fecha fue un miércoles"
        elif d == 3:
            resultado = "Tu fecha fue un jueves"
        elif d == 4:
            resultado = "Tu fecha fue un viernes"
        elif d == 5:
            resultado = "Tu fecha fue un sábado"
        elif d == 6:
            resultado = "Tu fecha fue un domingo"

        Resulatado.delete(0, END)
        Resulatado.insert(0, resultado)
        Resulatado.config(state="readonly")
        entrada_año.focus()

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número de año y mes válido.")

tk.Button(ventana, text="Calcular", command=calendario_gregoriano).place(x=20, y=260)

ventana.mainloop()





