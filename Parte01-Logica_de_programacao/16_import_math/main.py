#Importação da biblioteca math
import math

try:
    while True:
        r = float(input("Informe o valor do raio: ").replace(",", "."))
        area = math.pi*r**2
        print(f"A área do círculo é: {area:.2f} m2.")

        print("1 - Calcular ára de outro circulo")
        print("2 - Sair do programa")

        opcao = input("Informe a sua opção: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção inválida.")
except Exception as e:
    print("Não foi possível calcular. {e}")