import os
import math

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_fibonacci(n):
    return n if n <=1 else calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

"""
    lista_fibonacci = []
    if x == 0:
        lista_fibonacci.append(0)
        return lista_fibonacci
    elif x == 1:
        lista_fibonacci.append(0)
        lista_fibonacci.append(y + z)
        return lista_fibonacci
    else:
        lista_fibonacci.append(0)
        lista_fibonacci.append(y + z)
        while x > z:
             
            w = y + z
            y = z
            z = w
            lista_fibonacci.append(w)
            calcular_fibonacci(x, y, z)
        return lista_fibonacci
           
"""