import datetime
from datetime import date
from models import limpar, Conta

def hoje():
    return date.today().strftime("%d/%m/%y")

def agora():
    return datetime.datetime.now().strftime("%H:%M:%S")  

def main():
    limpar()
    cc = Conta(titular="", cpf="", agencia="1234-5", n_conta="10123-4", saldo=0.0)

    cc.titular = input("Informe o nome do titular da conta: ").strip().title()
    cc.cpf = input("Informe o CPF do titular da conta: ").strip()

    limpar()
    print(f"Conta criada no dia {hoje()} as {agora()}. ")

    while True:
        print("0 - Sair do programa.")
        print("1 - Consultar dados da conta.")
        print("2 - Fazer depósito.")
        print("3 - Fazer saque.")
        opcao = int(input("Informe a opção desejada. "))
        limpar()
        match opcao:
            case 0:
                break
            case 1:
                print(f"Data da consulta: {hoje()}.")
                print(f"Hora da consulta: {agora()}.")
                cc.consultar_conta()
            case 2:
                valor = float(input("Informe o valor do deposito: R$ ").replace(",", "."))
                if valor >=0:
                    print(f"Deposito efetuado com sucesso as {agora()} no dia {hoje()}" )
                    print(f"Saldo atual: R$ {cc.fazer_deposito(valor):2f}")
                else:
                    print("O depósio não pode ser efetuado:")
                continue                
            case 3:
                valor = float(input("Informe o valor do saque: R$ ").replace(",", "."))
                if valor >=0:
                    if valor <= cc.saldo:
                        print(f"Saque efetuado com sucesso as {agora()} do dia {hoje()}.")
                        print(f"Saldo atual; R$ {cc.fazer_saque(valor):2f}")
                    else:
                        print("Saldo insuficiente.")         
                else:
                    print("O valor não pode ser sacado.")
                    continue
            case _:
                print("Opcao inválida.")

if __name__ == "__main__":
    main()