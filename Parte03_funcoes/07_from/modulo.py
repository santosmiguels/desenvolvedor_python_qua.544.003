import os

#Função limpar a tela no prompt:
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#Função soma:
def somar(x, y):
    return x + y

#Função subtrair:
def subtrair(x, y):
    return x - y

#Função multiplicar:
def multiplicar(x, y):
    return x * y

#Função dividir:
def dividir(x, y):
    return x/y
