import os
import math

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#Calcular a área de um quadrilátero:
def area_quadrilatero (b, h):
    return b*h

#Calcular a área de um triângulo:
def area_triangulo (b, h):
    return (b*h)/2

#Calcular a área de um circulo:
def area_circulo (r):
    return math.pi*(r**2)

#Programa principal:

while True:
    limpar_tela()
    print("1 - Calcular área do quadrilátero.")
    print("2 - Calcular área do triângulo.")
    print("3 - Calcular área do círculo.")
    print("4 - Sair do programa.")
    opcao = int(input("Informe a opcao desejada: "))

    match opcao:
        case 1:
            b = float(input("Entre com o valor da base: ").replace(",", "."))
            h = float(input("Entre com o valor da altura: ").replace(",", "."))
            print(f"A área do quadrilatero é {area_quadrilatero(b, h)}")

        case 2:
            b = float(input("Entre com o valor da base: ").replace(",", "."))
            h = float(input("Entre com o valor da altura: ").replace(",", "."))
            print(f"A área do triângulo é {area_triangulo(b, h)}")

        case 3:
            r = float(input("Entre com o valor do raio: ").replace(",", "."))
            print(f"A área do triangulo é {area_circulo(r)}")

        case 4:
            break

        case _:
            print("Opção inválida:")
            continue