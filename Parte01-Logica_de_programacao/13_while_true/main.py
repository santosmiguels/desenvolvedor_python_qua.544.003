#Comando while e true
try:
    while True:
        nome = input("informe o nome do usuário: ")
        idade = int(input("Informe a idade do cliente: "))
        altura = float(input("Informa a altura do cliente: ")).replace(",", ".")
        if idade >= 12 and altura >= 1.25:
            print(f"A entrada do(a) {nome} está liberada.")
        else:
            print("Só é permitida a entrada de pessoas com mais de 12 anos e 1,25 metros.")

        print("1 - Passar novo pagante.")
        print("2 - Encerrar o programa")

        opcao = input("Informe a opcao desejada: ").strip

        match opcao:
            case "1":
                continue
            case "2":
                print("Fim do programa.")
                break
            case _:
                continue    
except:
    print("Não foi possível registrar a entrada do pagante.")