#TODO - atividade 03
#Crie um programa que recebea o nome de um aluno e 3 notas.
#O programa deve calcular a media do aluno e informar se:
#O aluno está aprovado se (média mínima = 7) ou reprovado.
#O programa deve gravar esses dados em um json.
#Ao final, o usuário deverá escolher se deseja inserir as 
#notas de outro aluno, que deverão ser gravadas no mesmoo arquivo json.

import os
import json

notas_dos_alunos = []
ficha = " "

while True:
    os.system("cls" if os.name == "nt" else "clear")
    alunos = {}
    aluno = input("Entre com o nome do aluno: ").strip().title()
    nota1 = float(input("Entre com a nota1: "))
    nota2 = float(input("Entre com a nota2: "))
    nota3 = float(input("Entre com a nota3: "))


    media = (nota1 + nota2 + nota3) / 3

    if media < 7:
        situacao = "Reprovado"
        print(f"(O aluno {aluno}) não foi aprovado com a media {media}.")
        alunos['aluno'] = aluno
        alunos['nota1'] = nota1
        alunos['nota2'] = nota2
        alunos['nota3'] = nota3
        alunos['media'] = media
        alunos['situacao'] = situacao
        print(alunos)
        notas_dos_alunos.append(alunos)
    else:
        situacao = "Aprovado"
        print(f"O aluno {aluno} está aprovado com a média {media}.") 
        alunos['aluno'] = aluno
        alunos['nota1'] = nota1
        alunos['nota2'] = nota2
        alunos['nota3'] = nota3
        alunos['media'] = media
        alunos['situacao'] = situacao
        print(alunos)
        notas_dos_alunos.append(alunos)

    

    print(notas_dos_alunos)

    with open(f"./{ficha}.json", "w", encoding="utf-8") as f:
        json.dump(notas_dos_alunos, f)
       
    opcao = input("Deseja inserir a nota de outro aluno (S/N)?").strip().upper()

    #with open(f"23_json/{arquivo}.json", "w", encoding="utf-8") as f:
    #with open(f"17_arquivos/arquivos/{nome_aquivo}.txt", "w", encoding="utf-8") as f:
        #f.write(usuarios)
        #json.dump(usuarios, f)
        

    if opcao == "S":
        continue
    else:
        break

for notas in notas_dos_alunos:
    #print(notas)
    #for estudante in notas:
    print("*"*40)
    print(f"Aluno: {notas['aluno']}")
    print(f"Nota1: {notas['nota1']}")
    print(f"nota2: {notas['nota2']}")
    print(f"nota3: {notas['nota3']}")
    print(f"Média: {notas['media']}")
    print(f"situação: {notas['situacao']}")
    #print("*"*40)

    """
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
"""
