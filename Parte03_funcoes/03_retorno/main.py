#Funções com parãmetros:

def boas_vindas (nome):
    #print(f"Seja Bem vindo, {nome} 👌🎶!")
    return f"Seja Bem vindo, {nome} 👌🎶!"


#programa principal:
import os
os.system = "cls" if os.name == 'nt' else "clear"
nome = input("Entre com o seu nome: ").strip().title()


print(boas_vindas(nome))