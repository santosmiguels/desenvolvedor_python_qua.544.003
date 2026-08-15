from modulo import limpar_tela, equacao_segundo_grau


def main():
    limpar_tela()

    a = int(input("entre com o valor de a:"))
    b = int(input("entre com o valor de b:"))
    c = int(input("entre com o valor de c:"))

    resultado = equacao_segundo_grau(a, b, c)

    print("Resolução da equação do segundo grau.")
    for valor in resultado:
        print(f"x = {valor}")

if __name__ == "__main__":
    main()

