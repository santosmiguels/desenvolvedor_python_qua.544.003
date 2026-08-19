# TODO - Atividade 05
# #Usando recursividade crie um programa onde o usuário informa um número inteiro e o programa calcula a sequência de Fibonacci até o número informado.
import modulo

modulo.limpar_tela()

def main():


    x = int(input("Entre com o número para calcular a sequência de Fibonacci: "))
    #y = 0
    #z = 1
    print(f"A sequência de Fibonacci de {x} é igual a {modulo.calcular_fibonacci(x)}")

if __name__ == "__main__":
    main()