def elegir_mes(valor):
    if valor == 1:
        print("Enero")
    elif valor == 2:
        print("Febrero")
    elif valor == 3:
        print("Marzo")
    elif valor == 4:
        print("Abril") 
    elif valor == 5:
        print("Mayo")
    elif valor == 6:
        print("Junio")
    elif valor == 7:
        print("Julio")
    elif valor == 8:
        print("Agosto")
    elif valor == 9:
        print("Septiembre")
    elif valor == 10:
        print("Octubre")
    elif valor == 11: 
        print("Noviembre")
    elif valor == 12:
        print("Diciembre") 
    else:
        print("Valor no valido")

print("Ingresar un numero del 1 al 12: ")
elegir_mes(int(input()))

# def elegir_mes(valor):
    
#     meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
#     if valor >= 1 and valor <= 12:
#         print(meses[valor - 1])
#     else:
#         print("Valor no valido")


