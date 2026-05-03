from tkinter import END,messagebox,ttk
import tkinter as tk

ventana=tk.Tk()
ventana.config(width=350,height=300)
ventana.title("Practica 10")

#Crear las variables para los checks

var1=tk.BooleanVar()
var2=tk.BooleanVar()
var3=tk.IntVar()
textoEtiqueta=""

#Labels superiores 

tk.Label(ventana, text="Tipo de Figura").place(x=20, y=0)
tk.Label(ventana, text="Valores").place(x=150, y=0)

#Crear los frames 

frame_cuadrado = tk.Frame(ventana)

tk.Label(frame_cuadrado, text="Lado:").grid(row=0, column=0)
lado_cuadrado = tk.Entry(frame_cuadrado, width=10)
lado_cuadrado.grid(row=0, column=1)


frame_rectangulo = tk.Frame(ventana)

tk.Label(frame_rectangulo, text="Base:").grid(row=0, column=0)
base_rectangulo = tk.Entry(frame_rectangulo, width=10)
base_rectangulo.grid(row=0, column=1)
tk.Label(frame_rectangulo, text="Altura:").grid(row=1, column=0)
altura_rectangulo = tk.Entry(frame_rectangulo, width=10)
altura_rectangulo.grid(row=1, column=1)

frame_triangulo = tk.Frame(ventana)

tk.Label(frame_triangulo, text="Base:").grid(row=0, column=0)
base_triangulo = tk.Entry(frame_triangulo, width=10)
base_triangulo.grid(row=0, column=1)
tk.Label(frame_triangulo, text="Altura:").grid(row=1, column=0)
altura_triangulo = tk.Entry(frame_triangulo, width=10)
altura_triangulo.grid(row=1, column=1)

frame_circulo = tk.Frame(ventana)

tk.Label(frame_circulo, text="Radio:").grid(row=0, column=0)
radio_circulo = tk.Entry(frame_circulo, width=10)
radio_circulo.grid(row=0, column=1)

def calcular():
    opcionSel = var3.get()

    if opcionSel == 1:
        frame_rectangulo.place_forget()
        frame_triangulo.place_forget()
        frame_circulo.place_forget()
        frame_cuadrado.place(x=150, y=30)
    elif opcionSel == 2:
        frame_cuadrado.place_forget()
        frame_rectangulo.place_forget()
        frame_circulo.place_forget()
        frame_triangulo.place(x=150, y=30)
    elif opcionSel == 3:    
        frame_cuadrado.place_forget()
        frame_triangulo.place_forget()
        frame_circulo.place_forget()
        frame_rectangulo.place(x=150, y=30)
    elif opcionSel == 4:
        frame_cuadrado.place_forget()
        frame_rectangulo.place_forget()
        frame_triangulo.place_forget()
        frame_circulo.place(x=150, y=30)

#crear los radios
radio1 = tk.Radiobutton(ventana, text="Cuadrado", variable=var3, value=1, command=calcular)
radio1.place(x=20, y=30)

radio2 = tk.Radiobutton(ventana, text="Triangulo", variable=var3, value=2, command=calcular)
radio2.place(x=20, y=60)

radio3 = tk.Radiobutton(ventana, text="Rectangulo", variable=var3, value=3, command=calcular)
radio3.place(x=20, y=90)

radio4 = tk.Radiobutton(ventana, text="Circulo", variable=var3, value=4, command=calcular)
radio4.place(x=20, y=120)

#Labels inferiores

tk.Label(ventana, text="Tipo de calculo").place(x=20, y=150)
tk.Label(ventana, text="Resultado").place(x=150, y=150)

#Caja de texto para mostrar el resultado
resultado = tk.Entry(ventana, width=20, state="readonly")
resultado.place(x=150, y=180)

def calcular_area():    
    opcionSel = var3.get()
    area = 0
    try:
        resultado.config(state="normal") # CORRECCIÓN AQUÍ
        resultado.delete(0, END)
        if opcionSel == 1:
            lado = float(lado_cuadrado.get())
            area = lado ** 2
        elif opcionSel == 2:
            base = float(base_triangulo.get())
            altura = float(altura_triangulo.get())
            area = 0.5 * base * altura
        elif opcionSel == 3:
            base = float(base_rectangulo.get())
            altura = float(altura_rectangulo.get())
            area = base * altura
        elif opcionSel == 4:
            radio = float(radio_circulo.get())
            area = 3.14159 * radio ** 2
        
        resultado.insert(0, f"Área: {area}")
        resultado.config(state="readonly") # VOLVEMOS A BLOQUEAR
    except ValueError:
        messagebox.showerror(message="Por favor, ingresa valores numéricos válidos.")
        return None
    

def calcular_perimetro():
    try:
        resultado.config(state="normal") # CORRECCIÓN AQUÍ
        resultado.delete(0, END)
        perimetro = 0
        opcionSel = var3.get()
        if opcionSel == 1:
            lado = float(lado_cuadrado.get())
            perimetro = 4 * lado
        elif opcionSel == 2:
            base = float(base_triangulo.get())
            altura = float(altura_triangulo.get())
            perimetro = base + 2 * altura 
        elif opcionSel == 3:
            base = float(base_rectangulo.get())
            altura = float(altura_rectangulo.get())
            perimetro = 2 * (base + altura)
        elif opcionSel == 4:
            radio = float(radio_circulo.get())
            perimetro = 2 * 3.14159 * radio
            
        resultado.insert(0, f"Perímetro: {perimetro}")
        resultado.config(state="readonly") # VOLVEMOS A BLOQUEAR
    except ValueError:
        messagebox.showerror(message="Por favor, ingresa valores numéricos válidos.")
        return None

def operacion_select():
    try:
         if var1.get()==True:
            calcular_area()
         elif var2.get()==True:
            calcular_perimetro()
    except Exception as e:
        messagebox.showerror(message=f"Elige un tipo de calculo: {str(e)}")
        return None

#crear los checks
check1 = tk.Checkbutton(ventana, text="Area", variable=var1, command=operacion_select)
check1.place(x=20, y=180)
check2 = tk.Checkbutton(ventana, text="Perimetro", variable=var2, command=operacion_select)
check2.place(x=20, y=210)

#Boton para calcular
tk.Button(ventana, text="Calcular", command=operacion_select).place(x=150, y=90)

#Boton para limpiar

tk.Button(ventana, text="Limpiar").place(x=240, y=90)

ventana.mainloop()