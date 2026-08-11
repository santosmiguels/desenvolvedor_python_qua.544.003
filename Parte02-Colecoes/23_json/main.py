#Gerar umjson.
#Abrir um json.

import json
import os

#Declarar variáveis
#Criar lista de usuários
usuarios = []
abrir = ""

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Gravar novo arquivo JSON.")
    print("2 - Gravar em arquivo JSON existente.")
    print("3 - Ler arquivo JSON.")
    print("4 - Sair do programa.")

    opcao = int(input("Escolha a opção desejada: "))
    os.system("cls" if os.name == "nt" else "clear")
    if opcao == 1 or opcao == 2:
        usuario = {}
        usuario['nome'] = input("informe o nome do usuário: ").strip().title()
        usuario['email'] = input("Informe o e-mail do usuário: ").strip().lower()
        usuarios.append(usuario)
        print(usuario)

        match opcao:
            case 1:
                arquivo = input("Entre com o nome do novo arquivo JSON: ")
                with open(f"23_json/{arquivo}.json", "w", encoding="utf-8") as f:
                #with open(f"17_arquivos/arquivos/{nome_aquivo}.txt", "w", encoding="utf-8") as f:
                    #f.write(usuarios)
                    json.dump(usuarios, f)
            case 2:
                if abrir:
                    #arquivo_existente = input("Entre com o nome do arquivo a ser para adiconar os dados: ")
                    with open(f"23_json/{abrir}.json", "w", encoding="utf-8") as f:
                        json.dump(usuarios, f)
                else:
                    abrir = input("Entre com o nome do arquivo JSON que deseja alterar: ")
                    with open(f"23_json/{abrir}.json", "r", encoding="utf-8") as f:
                        json.load()
                    with open(f"23_json/{abrir}.json", "w", encoding="utf-8") as f:
                        json.dump(usuarios, f)
    else:
        match opcao:
            case 3:
                abrir = input("Informe o nome do arquivo que deseja abrir: ")
                with open("23_json/{abrir}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
            case 4:
                break
            case _:
                print("Opção inválida.")
                continue