# - Modulo com funções 
# Import 
import os
from math import sqrt, pi

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#limpar = lambda: ("cls" if os.name == "nt" else "clear")

def calcular_potencia(x, y):
    return x**y

def calcular_raiz_quadrada(x):
    return sqrt(x)

def calcular_volume_paralelepipedo(x, y, z):
    return x*y*z

def calcular_volume_cilindro(r, h):
    return pi*(r**2)*h

