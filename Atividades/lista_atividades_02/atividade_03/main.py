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
