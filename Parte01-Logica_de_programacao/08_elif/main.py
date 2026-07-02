#Decaração de variáveis
nome = input("informe o nome de aluno: ")
nota = float(input("Informe a nota do aluno: ").replace(",", "."))

#Verificação se a nota é válida

if nota >=0 and nota <=10:
    if nota >= 7:
        print(f"{nome} está aprovado.")
    elif nota >=5:
        print(f"{nome} está de recuperação.")
    else:
        print(f"{nome} está reprovado")


        
    #Media em que ser maior que 7

    #print("Nota válida:  {nota}")
else:
    print(f"Nota de {nome} inválida.")