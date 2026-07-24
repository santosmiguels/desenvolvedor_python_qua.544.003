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
            nome_aquivo = input("Digite o nome do arquivo se a extenção: ").strip()
            #Grava novo arquivo:
            with open(f"17_arquivos/arquivos/{nome_aquivo}.txt", "w", encoding="utf-8") as f:
                f.write(novo_texto)
            print("Texto gravado com sucesso.")
        case "2":
            nome = input("Digite o nome do arquivo que deseja abrir: ").strip()
            try:
                with open(f"17_arquivos/arquivos/{nome}.txt", "r", encoding="utf-8") as f:
                    nome = f.read()
                print(nome)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            continue
        case "3":
            novo_texto = input("Digite o texto a ser acrescentado: ").strip()
            #nova_gravacao = f"{}"
            try:
                with open(f"17_arquivos/arquivos/{nome_alterar}.txt", "r", encoding="utf-8") as f:
                    alterar = f.read()
                print(alterar)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            continue
        case "4":
            break
        case "_":
            print("Opção inválida.")
            continue

#os.system("cls" if os.name == "nt" else "clear")
