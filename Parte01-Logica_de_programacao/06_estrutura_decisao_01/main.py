nome = input("Informe o seu nome: ").title()
idade = int(input("Informe a sua idade: "))

if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")