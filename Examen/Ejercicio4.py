from tkinter import Tk , messagebox, END 
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora IMC")
ventana.geometry("300x600")

#Ingresar Peso y Altura 

tk.Label(ventana, text = "CALCULE SU INDICE DE MASA CORPORAL").pack(pady=5)
tk.Label(ventana, text = "INGRESE SU PESO EN KG").pack(pady=5)
entrada_peso = tk.Entry(ventana, state = "normal")
entrada_peso.pack(pady=5)
tk.Label(ventana, text = "INGRESE SU ALTURA EN METROS").pack(pady=5)
entrada_altura = tk.Entry(ventana, state = "normal")
entrada_altura.pack(pady=5)
tk.Label(ventana, text = "RESULTADO").pack(pady=5)
salida_resultado= tk.Entry(ventana, state = "readonly")
salida_resultado.pack(pady=5)
tk.Label(ventana,text ="")

tipo_categoria = ""
Etiqueta = tk.Label(ventana,text = tipo_categoria)
Etiqueta.pack(pady=5)

def calculo_IMC(categoria):
    try:  
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())

        imc = peso/(altura*altura)

        salida_resultado.config(state="normal")
        salida_resultado.delete(0,END)
        salida_resultado.insert(0, imc)
        salida_resultado.config(state ="readonly")

        if imc < 18.5:
            tipo_categoria = "Bajo Peso"
        if imc <25:
            tipo_categoria = "Normal"
        if imc <30:
            tipo_categoria = "Sobrepeso"
        if imc >30:
            tipo_categoria = "Obesidad"
        Etiqueta.config(text= tipo_categoria)
    except:
        messagebox.showerror("Ingresa un valor numerico valido")

def limpiar():
    salida_resultado.config(state= "normal")
    salida_resultado.delete(0, END)
    entrada_altura.delete(0,END)
    entrada_peso.delete(0,END)
    salida_resultado.config(state="normal")


tk.Button(ventana,text="Calcular",command=lambda:calculo_IMC(Etiqueta)).pack(pady=5)
tk.Button(ventana,text="Limpiar",command=limpiar).pack(pady=5)

ventana.mainloop()




