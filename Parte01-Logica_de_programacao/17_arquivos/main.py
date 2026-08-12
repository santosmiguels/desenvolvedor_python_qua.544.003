# Criar arquivos de texto
import os

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Gravar arquivo")
    print("2 - Ler arquivo")
    print("3 - Alterar um texto")
    print("4 - sair")

    opcao = input("informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            novo_texto = input("Digite o seu texto: ")
            nome_arquivo = input("Digite o nome do arquivo se a extenção: ").strip()
            #Grava novo arquivo:
            with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
                f.write(novo_texto)
            print("Texto gravado com sucesso.")
        case "2":
            nome = input("Digite o nome do arquivo que deseja abrir: ").strip()
            print({nome})
            try:
                with open(f"17_arquivos/arquivos/{nome}.txt", "r", encoding="utf-8") as f:
                    nome = f.read()
                print(nome)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            continue
        case "3":
            novo_texto = input("Digite o texto a ser acrescentado: ").strip()
            nome_abrir = input("Digite o nome do arquivo que deseja abrir para alterar: ").strip()
            try:
                with open(f"17_arquivos/arquivos/{nome_abrir}.txt", "r", encoding="utf-8") as f:
                    nome_abrir = f.read()
                print(nome_abrir)
                print(novo_texto)

            except FileNotFoundError:
                print("Arquivo não encontrado.")
            continue
        case "4":
            break
        case "_":
            print("Opção inválida.")
            continue

#os.system("cls" if os.name == "nt" else "clear")
