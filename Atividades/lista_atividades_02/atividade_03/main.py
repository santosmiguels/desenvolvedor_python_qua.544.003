#TODO - atividade 03
#Crie um programa que recebea o nome de um aluno e 3 notas.
#O programa deve calcular a media do aluno e informar se:
#O aluno está aprovado se (média mínima = 7) ou reprovado.
#O programa deve gravar esses dados em um json.
#Ao final, o usuário deverá escolher se deseja inserir as 
#notas de outro aluno, que deverão ser gravadas no mesmo arquivo json.

import os
import json

#Declaração de variáveis1

notas_dos_alunos = []
#fichario = "fichario"

os.system("cls" if os.name == "nt" else "clear")
#Laço de repetição até concluir o cadastro de notas:
while True:
  
    #Início da tela do sistema:
    print("Sistema de entrada de notas para os alunos do curso:")
    print("1 - Entrar com as notas dos alunos.")
    print("2 - sair.")
    opcao_de_entrada = int(input("Escolha a opção desejada:"))

    match opcao_de_entrada:
        case 1:
            
            #Recebimento dos dados dos alunos:
            os.system("cls" if os.name == "nt" else "clear")
            alunos = {}
            aluno = input("Entre com o nome do aluno: ").strip().title()
            nota1 = float(input("Entre com a nota1: ").replace(",", "."))
            nota2 = float(input("Entre com a nota2: ").replace(",", "."))
            nota3 = float(input("Entre com a nota3: ").replace(",", "."))

            #Cálculo da média das notas:
            media = (nota1 + nota2 + nota3) / 3

            #Verificação da situação do aluno: 
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

            #mostrar na tela a lista com os dados preenchidos;
            print(notas_dos_alunos)

            #Gravar/acrescentar os dados de um aluno no arquivo .json:
            with open("fichario.json", "w", encoding="utf-8") as f:
                json.dump(notas_dos_alunos, f)

            #Verificar se continua a dicçao de outro aluno e suas notas:       
            opcao = input("Deseja inserir a nota de outro aluno (S/N)?").strip().upper()        

            if opcao == "S":
                continue
            else:
                break


        case 2:
            break
        case _:
            print("Opção inválida.")

#limpa a tela e mostra na tela os dados inseridos:
os.system("cls" if os.name == "nt" else "clear")
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