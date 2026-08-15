#Declaração das variávei;
from modulo import limpar_tela, somar, subtrair

def main():


    while True:
        limpar_tela()
        print("Sistema calculadora:")
        print("1 - Operação somar.")
        print("2 - Operação subtrair.")
        print("3 - Operação multiplicar.")
        print("4 - Operação dividir.")
        print("5 - Sair do sistema.")

        opcao = int(input("Entre com a operação desejada: "))

        match opcao:
            case 1:
                x = float(input("Digite o valor de x: "))
                y = float(input("Entre com o valor de x: "))
                print(somar(x, y))
                continuar = input("Deseja fazer outra operação (S/N)?").strip().upper()
                if continuar == "S":
                    continue
                else:
                    break
            case 2:
                x = float(input("Digite o valor de x: "))
                y = float(input("Entre com o valor de x: "))
                print(subtrair(x, y))
            case 3:
                pass
            case 4:
                pass
            case 5:
                break
            case _:
                print("Opção inválida")
        
if __name__ =="__main__":
    main()