#Declaração de variáveis
nome = input("informe o seu nome: ")
telefone = input("Informe o seu telefone: ")

#Saída de dados
#print("Olá ", nome ", e o meu telefone é ", telefone,".")
#print("Olá ", + nome + ",e meu telefone é " + telefone + ".")
print("Olá {}, e meu telefone é {}.".format(nome, telefone))
print(f"Olá {nome}, e meu telefone é {telefone}.")