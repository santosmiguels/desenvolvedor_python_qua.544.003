#Declaração de variáveis:
nome = input("Informe o seu nome: ").title()
idade = int(input("Informe a sua idade: "))

#Saída de dados com operador ternário:
print(f"{nome} é maior de idade" if idade >= 18 else f"{nome} é menor de idade. ")
