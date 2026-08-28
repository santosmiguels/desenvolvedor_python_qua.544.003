import models

def main():
    pedido = models.Pedido(valor1=0.0,valor2=0.0)

    models.limpar()

    models.Pedido.valor1 = float(input("Informe a valor 1: ").replace(",", "."))
    models.Pedido.valor2 = float(input("Informe o valor 2: ").replace(",","."))

    print("1 - Somar.")
    print("2 - Subtrair.")
    print("3 - Multiplicar.")
    print("4 - Dividir.")

    operador = input("Informe a operação desejada: ").strip()

    print(pedido.calcular_total(operador=operador))

if __name__ == "__main__":
    main()