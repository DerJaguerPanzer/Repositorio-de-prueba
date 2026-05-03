from tkinter import END, messagebox, ttk
import tkinter as tk

ventana = tk.Tk()
ventana.config(width=300,height=350)
ventana.title("Calculadora")

ttk.Label(ventana,text="Selecciona una opccion").place(x=20,y=20)
cbCategorias = ttk.Combobox(ventana, state="readonly", values=["A","B","C","D"])
cbCategorias.place(x=20,y=50)

def evaluar():
    # imagen = tk.PhotoImage(file="ejemplo.png")
    # label = tk.Label(ventana, image=imagen)
    # label.place(x=20, y=300) # Posición de la imagen en la ventana
    opcion = cbCategorias.get()
    if opcion == "A":
        messagebox.showinfo(message="Elegiste la opcion A")
    elif opcion == "B":
        messagebox.showinfo(message="Elegiste la opcion B")
    elif opcion == "C":
        messagebox.showinfo(message="Elegiste la opcion C")
    elif opcion == "D":
        messagebox.showinfo(message=f"Elegiste la opcion D ")

ttk.Button(ventana, text="Aceptar", command=evaluar).place(x=20,y=80)

ventana.mainloop()
