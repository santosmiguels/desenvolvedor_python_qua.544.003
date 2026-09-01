import models

def main():
    titular = models.Pessoa(nome="",cpf="")

    conta_corrente = models.Conta(agencia="",n_conta="",saldo=0.0,pessoa="")

    titular.nome = input("Entre com o nome do titular: ")
    titular.cpf = input("Entre com o CPF do titular: ")

    #conta_corrente.agencia = input("Entre com o número da agência: ")
    #conta_corrente.n_conta = input("Entre com o número da conta corrente: ")
    #conta_corrente.saldo = int(input("Entre com o saldo atual da conta: "))

    #models.consultar_dados()

if __name__ == "__main__":
    main()