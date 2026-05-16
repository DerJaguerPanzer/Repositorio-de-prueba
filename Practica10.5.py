from tkinter import END, messagebox, ttk 
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("180x180")
ventana.title("Practica 10.5")

ttk.Label(ventana, text="Introduce un numero a buscar").pack(pady=5)
caja = ttk.Entry(ventana)
caja.pack(pady=5)

lista = [12 , 45 , 7 , 23 , 89, 4 , 56 , 17]

def buscar_valor():
    try:
        buscado = int(caja.get())
        i = 0 
        encontrado = False 
        while i < len(lista):
            if lista[i] == buscado:
                encontrado = True
                break
            i+=1
        if encontrado == True:
            messagebox.showinfo("Resultado", f"El valor se encuentra en la posicion {i}")
        else: 
            messagebox.showwarning("No encontrado", "El valor no esta en la lista")
    except:
        messagebox.showerror("Error","Ingresa un valor valido")
        
def mostrar_maximo():
        maximo = max(lista)
        # messagebox.showinfo("Maximo", "El valor maximo de la lista es: " + str(maximo)) Otra forma de hacerlo
        messagebox.showinfo("Maximo", f"El valor maximo de la lista es: {maximo}")
        
def abrir_modal():
    modal = tk.Toplevel(ventana)
    modal.title("Añade un Valor")
    modal.grab_set() # Esto hace que la ventana modal sea modal, es decir, que el usuario no pueda interactuar con la ventana principal hasta que cierre la modal.
    
    ttk.Label(modal, text="Introduce un numero a añadir").pack(pady=5)
    entrada_modal = ttk.Entry(modal)
    entrada_modal.pack(pady=5)
    
    def agregar():
        try:
            nuevo=int(entrada_modal.get())
            lista.append(nuevo)
            messagebox.showinfo("Exito", f"Valor {nuevo} agregado a la lista")
        except:
            messagebox.showerror("Error", "Ingresa un valor valido")
            
    ttk.Button(modal, text="Agregar", command=agregar).pack(pady=5)
    

ttk.Button(ventana, text="Buscar", command= buscar_valor).pack(pady=5)
ttk.Button(ventana, text="Mostrar Maximo", command= mostrar_maximo).pack(pady=5)
ttk.Button(ventana, text="Añadir un valor", command=abrir_modal).pack(pady=5)


#.pack es un método de geometría que se utiliza 
# para organizar los widgets en la ventana en vertical u horizontal. 
# En este caso, se utiliza para colocar la etiqueta y la caja de entrada en la ventana 
# con un espacio vertical de 5 píxeles entre ellos.


ventana.mainloop()