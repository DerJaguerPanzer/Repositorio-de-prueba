# #Listas 

# milista = ["Maria", "Jose","Martha",3.1416]

# print(milista[2:]) #Imprime desde el indice 2 hasta el final de la lista
# print(milista[:3]) #Imprime desde el inicio de la lista hasta el indice 3 (sin incluirlo)
# print(milista[1:3]) #Imprime desde el indice 1 hasta el indice 3 (sin incluirlo)

# milista.append(True) #Agrega un elemento al final de la lista
# print(milista)

# milista.insert(2,"Juan") #Agrega un elemento en la posicion indicada
# print(milista)

# print(dir(milista)) #Muestra los metodos disponibles para las listas


# milista.extend(["Cosme","Fulanito",False,17]) #Agrega los elementos de otra lista al final de la lista
# print(milista)

# print(milista.index("Maria")) #Muestra el indice de la primera ocurrencia del elemento indicado

# print("Fulanito" in milista) #Muestra si el elemento indicado está en la lista

# milista.append("Maria")

# milista.append("Martha")

# print(milista.count("Maria")) #Cuenta cuantas veces aparece el elemento indicado en la lista

# milista.remove(3.1416) #Elimina la primera ocurrencia del elemento indicado

# milista.pop(2) #Elimina el elemento en la posicion indicada y lo devuelve

# milista2 = ["Mexico","USA","Canada"] * 3
# # milista3 = milista + milista2 #Concatena dos listas
# # print(milista3)


# # Tuplas

# mitupla = ("Juan",13,3.14,2015)

# print(mitupla[2])

# print(dir(mitupla))

# milista5 = list(mitupla) #Convierte una tupla en una lista
# print(milista5)

# mitupla2 = tuple(milista5) #Convierte una lista en una tupla
# print(mitupla2)

# mitupla3 = mitupla + ("Maria",) #Concatena dos tuplas

# #Tupla unitaria 

# mituplaU = ("Solo un elemento",) #Para crear una tupla con un solo elemento, se debe agregar una coma al final
# print(len(mituplaU))

# mitupla6 = "Juan", 15, 10, True #Otra forma de crear una tupla sin usar paréntesis
# print(mitupla6)

# nombre, dia, mes, Casado = mitupla6 #Desempaquetado de tuplas
# print(nombre)
# print(dia)
# print(mes)
# print(Casado)

#Diccionarios 

# midiccionario = {"Alemania":"Berlin","Francia":"Paris","Mexico":"CDMX","España":"Madrid"}
# print(midiccionario["Mexico"]) #Accede al valor asociado a la clave indicada

# midiccionario["Italia"] = "Roma" #Agrega un nuevo par clave-valor al diccionario
# print(midiccionario)

# midiccionario = {"Numero":23,"Apelido":"Jordan","Equipo":"Chicago","Campeonatos":{ "Temporadas": [1991,1992,1993,1996,1997,1998] }}

# print(midiccionario["Campeonatos"]["Temporadas"][1]) #Accede al valor asociado a la clave "Temporadas" dentro del diccionario anidado "Campeonatos"

#Condicionales

# print ("Programa de evaluacion de alumnos")
# nota_alumno = float(input("Ingresa la nota del alumno: "))

# def evaluacion(nota):
#     status = "Aprobado"
#     if nota < 5:
#         status = "Reprobado"
#     return status
    
# print(evaluacion(nota_alumno))


#Ciclos
#FOR

email = input("Ingresa tu email: ")

for i in range(len(email)):
    if email[i] == "@" or email[i] == ".":
        email = True
        break
    else:
        email = False
        
if email:
    print("El email es valido")
else:
    print("El email no es valido")

# for i in range(1,11,2):
#     print(f"La tabla del dos es {i} x 2 = {i*2}")


