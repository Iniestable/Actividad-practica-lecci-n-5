from functools import reduce
import pdb

def numero_mayor(a, b):
    if (a > b):
        return a 
    else:
        return b


lista_1 = [2, 4, 1]

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8]

lista_3 = [100, 250, 43]

pdb.set_trace()
resultado_1 = reduce(numero_mayor, lista_1)

resultado_2 = reduce(numero_mayor, lista_2)

resultado_3 = reduce(numero_mayor, lista_3)

print (f"El numero más grande de la primera lista es: {resultado_1}, el de la segunda: {resultado_2}, y el de la tercera: {resultado_3}")  