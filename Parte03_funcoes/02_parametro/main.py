#Funções com parãmetros:

def boas_vindas (nome):
    print(f"Seja Bem vindo, {nome} 👌🎶!")
    #return


#programa principal:
nome = input("Entre com o seu nome: ").strip().title()

boas_vindas(nome)