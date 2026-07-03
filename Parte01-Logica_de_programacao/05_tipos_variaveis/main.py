#Declaração de variáveis.
nome = input("Informe o seu nome: ").title()
idade = int(input("Informe a sua idade: "))
altura = float(input("Informe a sua altura em metros: ").replace(",", "."))

#Saída de dados
print(f"O seu nome é {nome}. {type(nome)}")
print(f"Sua idade é {idade}.{type(altura)}")
print(f"Sua altura é {altura} m. {type(altura)}")