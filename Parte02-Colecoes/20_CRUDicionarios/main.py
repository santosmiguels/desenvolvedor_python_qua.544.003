#importar biblioteca:
import os

#Criar lista:

usuarios = []
os.system("cls" if os.name == "nt" else "clear")
while True:
    #Menu de opções:
    print(f"{'-'*20} CRUDicionario {'-'*20}")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Alterar dados de um usuário")
    print("4 - Apagar um usuário")
    print("5 - Sair")
    opcao = input("Escolha a opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            usuario = {
                'nome': "",
                'cpf': "",
                'email': ""
            }
            usuario['nome'] = input("Digite o nome do usuário: ").strip()
            usuario['cpf'] = input("Digite o cpf do usuário: ").strip()
            usuario['email'] = input("Digite o email do usuário: ").strip().lower()

            #Adiciona dicionário na lista
            usuarios.append(usuario)
            print(usuarios)
            continue
        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            continue
        case "3":
            nome = input("Informe o nome a ser pesquisado: ").strip().title()
            for usuario in usuarios:
                if nome in usuario['nome']:
                    #2º menu:
                    print("nome:")
                    print("CPF:")
                    print("email:")
                    print("Cancelar")
                    alterar = input("Qual a chave para ser alterada: ").strip().lower()
                    if alterar in usuario:
                        usuario[alterar]  = input("Informe o novo valor: ").strip()
                    else:
                        pass

                    print("alterado com sucesso")

                else:
                    print("Usario não encontrado.")
            continue
        case "4":
            nome = input("Informe o nome a ser deletado: ").strip().title()
            for usuario in usuarios:
                if nome in usuario['nome']:
                    usuarios.remove(usuario)
                    print("Usuario apagado com sucesso.")
                else:
                    print("Usuario não encontrado.")
            continue
        case "5":
            break
        case _:
            print("Opção inválida.")
            continue