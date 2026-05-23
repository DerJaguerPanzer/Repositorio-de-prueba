#Congruencia de zeller 

class Calculadora_calendario:

    def __init__(self):
        pass

    def calendario_gregoriano():


        año = int(input("Introduzca el año "))
        mes = int(input("Introduzca el mes "))
        dia = int(input("Introduzca el dia "))

        a = (14 - mes) // 12
        y = año - a
        m = mes + 12 * a - 2

        d = (5 + dia + y + y // 4 + (31 * m) // 12) % 7

        if d == 0:
            print("Tu fecha fue un lunes")
        elif d == 1:
            print("Tu fecha fue un martes")
        elif d == 2:
            print("Tu fecha fue un miércoles")
        elif d == 3:
            print("Tu fecha fue un jueves")
        elif d == 4:
            print("Tu fecha fue un viernes")
        elif d == 5:
            print("Tu fecha fue un sábado")
        elif d == 6:
            print("Tu fecha fue un domingo")
        else:
            print(f"Valor incorrecto")





