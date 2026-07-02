#Progrma mini calculadora.

#Declaração de variáveis:

x = float(input("Informe o valor de x: ").replace(",", "."))
y = float(input("Informe o valor de y: ").replace(",", "."))

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Informar a opçao desejada: ").strip()

match opcao: 
    case "1":
        print(f"A soma é: {x+y}")
    case "2":
        print(f"A subtração é: {x-y}")
    case "3":
        print(f"A multiplicação e: {x*y}")
    case "4":
        print(f"A divisão é: {x/y}")
    case _:
        print("Opcão inválida.")

'''
valor1 = "10"
valor2 = 10

try:
    print(valor1 + valor2)
except Exception as e: 
    print(f"Não foi possível rodar o programa. {e}.")
finally:
    print('Tente mudar o valor da variável "valor1" para um número inteiro caso dê erro')
'''