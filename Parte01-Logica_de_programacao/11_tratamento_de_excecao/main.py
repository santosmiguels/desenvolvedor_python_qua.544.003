'''
#Declaração de variáveis e entrada de dados
n= int(input("Informe um número intero: "))

#Saída de dados
print(f"Número informado: {n}.")
'''

#Tratamento de excecao
try:
    #Declaração de variáveis.
    n = int(input("Informe um número inteiro: "))

    #Saída de dados
    print(f"Número informado: {n}.")
except:
    print("O código não pode ser excutado. Observe se a entrada dos dados está de acordo.")