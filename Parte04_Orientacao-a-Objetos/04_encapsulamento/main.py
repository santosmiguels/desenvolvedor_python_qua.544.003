#O encapsulamento é uma proteção que coloca na classe.
#Forma indireta.
import models

def main():
    models.limpar()
    usuario = models.Pessoa(nome="", cpf="", email="", telefone="")

    #Método set:
    usuario.nome = input("Entre com o nome de usuário: ").strip().title()
    usuario.cpf = input("Digite o CPF do usuário: ").strip()
    usuario.email = input("Informe o email do usuário: ").strip()
    usuario.telefone = input("Entre com o telefone do usuário: ").strip()

    models.limpar()

    print("A ficha do usuário pedido é: ")
    print(f"nome: {usuario.nome}")
    print(f"cpf: {usuario.cpf}")
    print(f"email: {usuario.email}")
    print(f"telefone: {usuario.telefone}")

    #Método get:

if __name__ == "__main__":
    main()