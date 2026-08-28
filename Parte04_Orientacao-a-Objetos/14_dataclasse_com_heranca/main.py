import os
from models import PessoFisica,PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoFisica(nome="",cpf="",profissao="",idade=0,salario=0.0,telefone="",email="")
    empresa = PessoaJuridica(razao_social="",nome_fantasia="",cnpj="",valor_mercado=0.0,telefone="",email="")
    limpar()
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.profissao = input("Informe a profissão: ").strip()
    usuario.idade = int(input("Informe a idade: "))
    usuario.telefone = input("Entre com o telefone: ")
    usuario.email = input("Informe a e-mail do usuario: ")
    usuario.salario = float(input("Informe a salario do usuário: R$").replace(",","."))
    limpar()
    empresa.razao_social = input("Informe a razão social da empresa: ").strip().title()
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Entre com o CNPJ da empesa: ").strip()
    empresa.valor_mercado = float(input("Entre com valo de mercado da empresa: ").replace(",","."))
    empresa.email = input("entre com o e-mail da empresa: ").strip()
    empresa.telefone = input("Entre com o telefone da empresa: ").strip()

    print(usuario)
    print(empresa)

    del(usuario)
    del(empresa)

if __name__ == "__main__":
    main()