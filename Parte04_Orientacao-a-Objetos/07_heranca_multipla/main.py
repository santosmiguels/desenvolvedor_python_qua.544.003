import os
from models import Filho

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    #junior = Filho(nome="", cpf="", email="", telefone="", profissao="", peso=0.0, altura=0.0, olhos="", cabelo="")
    junior = Filho(nome="", cpf="", email="", telefone="", profissao="")
    limpar()
    junior.nome = input("Entre com o nome: ")
    junior.cpf = input("Entre com o CPF: ")
    junior.email = input("Entre com o e-mail: ")
    junior.telefone = input("Entre com o telefone: ")
    junior.profissao = input("Entre com a profissão: ")
    junior.peso = float(input("Entre com o peso: "))
    junior.altura = float(input("Entre com a altura: "))
    junior.olhos = input("Entre com a cor dos olhos: ")
    junior.cabelo = input("Entre com a cor dos cabelos: ")
    limpar()
    junior.exibir_dados()
    junior.mostrar_fisico()

if __name__ == "__main__":
    main()