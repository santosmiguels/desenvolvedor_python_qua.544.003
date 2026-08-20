#Criar o programa principal
import os
from models import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()

def main():
    homem = Pessoa(nome="", idade=0, email= "", telefone="")
    mulher = Pessoa(nome="", idade=0, email="", telefone="")

    homem.nome = input("Entre com o nome do homem: ").strip().title()
    homem.idade = int(input("Entre com a idade do homem: "))
    homem.email = input("Entre com o email do homem: ").strip().lower()
    homem.telefone = input("Entre com o telefone do homem: ").strip()

    mulher.nome = input("Entre com o nome da mulher: ").strip().title()
    mulher.idade = int(input("ntre com a idade da mulher: "))
    mulher.email = input("Entre com o email da mulher: ").strip().lower()
    mulher.telefone = input("Entre com o telefone da mulher: ").strip()

    limpar()
    print(homem.apresentar())

    print(mulher.cumprimentar(homem.nome))

    print(homem.cumprimentar(mulher.nome))

if __name__ == "__main__":
    main()