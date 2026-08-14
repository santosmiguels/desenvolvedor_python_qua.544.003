import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def equacao_primeiro_grau (a, b):
    #a*x + b = 0
    x = -b/a
    return(-b/a)

