from models import  PessoaFisica, PessoaJuridica, limpar

def main():
    limpar()

    usuario = PessoaFisica(nome="", cpf="", email="", telefone="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", email="", telefone="")

    usuario.nome = input("Entre com o nome do usuário: ").strip().title()
    usuario.cpf = input("Entre com o cpf do usuário: ").strip()
    usuario.email = input("Entre com o email do usuário: ").strip()
    usuario.telefone = input("Entre com o telefone do usuário:").strip()

    limpar()

    empresa.nome_fantasia = input("Entre com o nome fantasia da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Entre com o email da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    print("Esta é ficha do usuário e da empresa: ")

    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Email: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")

    print(f"Nome fantasia: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Email: {empresa.email}")
    print(f"Telefone: {empresa.telefone}")

if __name__ == "__main__":
    main()