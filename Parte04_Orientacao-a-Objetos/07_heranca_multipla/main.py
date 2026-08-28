import os
from models import Filho

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    junior = Filho(
        nome="", cpf="", email="", telefone="", profissao="", peso=0.0, altura=0.0, olhos="", cabelo="")
    
    limpar()

    junior.nome = input("Entre com o nome: ").strip().title()
    junior.cpf = input("Entre com o CPF: ").strip()
    junior.email = input("Entre com o e-mail: ").strip().lower()
    junior.telefone = input("Entre com o telefone: ").strip()
    junior.profissao = input("Entre com a profissão: ").strip()
    junior.peso = float(input("Entre com o peso: ").replace(",", "."))
    junior.altura = float(input("Entre com a altura: ").replace(",", "."))
    junior.olhos = input("Entre com a cor dos olhos: ").strip()
    junior.cabelo = input("Entre com a cor dos cabelos: ").strip()

    limpar()

    junior.exibir_dados()
    junior.mostrar_fisico()

if __name__ == "__main__":
    main()