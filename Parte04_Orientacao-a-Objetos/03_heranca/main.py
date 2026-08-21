#Herança ou generalização.
import os
import models

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    usuario = models.PessoaFisica(nome="", cpf="", email="", telefone="", endereco="")
    empresa = models.PessoaJuridica(razao_social="", nome_fantasia="", cnpj="", email="", telefone="", endereco="")

    usuario.nome = input("Entre com o nome do usuário: ").strip().title()
    usuario.cpf = input("Entre com o CPF do usuário: ").strip().title()
    usuario.email = input("entre com o e-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()
    usuario.endereco = input("Informe o endereço do usuário: ")

    limpar()
    
    empresa.razao_social = input("Entre com a razao social da empresa: ").strip()
    empresa.nome_fantasia = input("Entre com o nome fantasia da empresa: ").strip()
    empresa.cnpj = input("Entre com o CNPJ da empresa: ").strip()
    empresa.email = input("entre com o e-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ")

    limpar()
    usuario.exibir_dados()
    empresa.exibir_dados()

if __name__ == "__main__":
    main()