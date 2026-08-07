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
            usuario['email'] = input("Digite o nome do usuário: ").strip().lower()

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
            continue
        case "4":
            continue
        case "5":
            break
        case _:
            print("Opção inválida.")
            continue

"""
#print(usuarios)
for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")
"""