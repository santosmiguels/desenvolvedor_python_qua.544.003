# TODO - ATIVIDADE 04:
# Utilizando o conceito de módulo, crie um módulo com funçoes que façam as seguintes ações:
#Limpar o terminal;
# Calcule a potência de um número informado pelo usuário, elevando a outro número informado pelo usuário;
#Calcular a raiz quadrada de um número informado pelo usuário;
#Calcular o volume de um recipiente paralelepipídico;
#calcular o volume de um recipiente cilíndrico;
#Em seguida, faça um programa que  usuário escolha executar uma dessas funções ou sair do programa.

#importa as funçoes do modulo:
import modulo
#Declaração de variáveis:
modulo.limpar_tela()
#modulo.limpar
#Laço de repetição até que seja escolhida a função sair.
while True:
    print("Programa de calcular algumas fuções matemáticas.")
    print("1 - Calcular a potência de um número.")
    print("2 - Calcular a raiz quadrada de um número.")
    print("3 - Calcular o volume de um cubo.")
    print("4 - Calcaula o volume de um cilindro.")
    print("5 - Sair do programa.")
    opcao = int(input("Digite a opcao desejada: "))
    match opcao:
        case 1:
            print("Função que calcula a potência de um número.")
            x = int(input("Entre com o valor do número: "))
            y = int(input("Entre com a potência do número: "))
            print(f"O resultado de {x} elevado a {y} é igual a {modulo.calcular_potencia(x, y)}")
        case 2:
            print("Função que calcula a raiz quadrada de um número.")
            x = int(input("Entre com um número para calcular a raiz quadrada: "))
            print(f"A raiz quadrada de {x} é igual a {modulo.calcular_raiz_quadrada(x)}.")
        case 3:
            print("Função que calcula o volume de um paralelepípedo.")
            x = int(input("Entre com a base do paralelepípedo: "))
            y = int(input("Entre com a altura do paralelepípedo: "))
            z = int(input("Entre com a profundidade do paralelepípedo: "))
            print(f"O volume do paralelepípdo com {x}, {y} e {z} é igual a {modulo.calcular_volume_paralelepipedo(x, y, z)}.")
        case 4:
            print("Função de calcular o volume de um cilindro.")
            r = int(input("entre com o raio de um cilindro: "))
            h = int(input("Entre com a altura do cilindor: "))
            print(f"O volume do cilindro com raio {r} e altura {h} é igual a {modulo.calcular_volume_cilindro(r, h )}")
        case 5:
            break
        case _:
            print("Opcão inválida.")
#Saída do laçõ de repetição.
modulo.limpar_tela()
