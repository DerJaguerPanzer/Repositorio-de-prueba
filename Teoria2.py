# def generaPares(limite):
#     num = 1
#     while num < limite:
#         yield num * 2
# #         num += 1
# #     #return milista 

# # print(generaPares(10)) 

# # devuelvePares = generaPares(10)
# # # for i in devuelvePares:
# # #     print(i)    
# # print(next(devuelvePares))
# # print(next(devuelvePares))
# # print(next(devuelvePares))

# def devuelveCuadrados(*ciudades):
#     for i in ciudades:          # recorre cada ciudad
#         for letra in i:         # recorre cada letra de esa ciudad
#             yield letra.upper()  # devuelve la letra en mayúscula

# devuelveCuadrados("Madrid", "Barcelona", "Valencia")

# CON for anidado normal
def devuelveCiudades(*ciudades):
    for i in ciudades:
        for letra in i:
            yield letra

# EQUIVALENTE con yield from
def devuelveCiudades(*ciudades):
    for i in ciudades:
        yield from i    # ← itera y hace yield de cada letra automáticamente