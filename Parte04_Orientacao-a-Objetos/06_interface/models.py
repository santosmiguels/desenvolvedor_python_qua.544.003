#Interface ´um conjunto de regras que  classe tem que seguir.
import os
from abc import ABC, abstractclassmethod

def limpar():
    os.system("cls" if os.name == "nt" else "class")

class Iconta(ABC):
    @abstractclassmethod
    def consultar_conta():
        pass

    @abstractclassmethod
    def fazer_deposito(valor):
        pass

    @abstractclassmethod
    def fazer_saque(valor):
        pass

class Conta(Iconta):
    def __init__(self, titular, cpf, agencia, n_conta, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def n_conta(self):
        return self.__n_conta

    @n_conta.setter
    def n_conta(self, n_conta):
        self.__n_conta = n_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo  

    def consultar_conta(self):
        print(f"Nome do titular da conta: {self.__titular}")
        print(f"CPF do titular da conta: {self.__cpf}")
        print(f"Agência da conta: {self.__agencia}")
        print(f"Número da conta: {self.n_conta}")
        print(f"Saldo da conta: {self.saldo}")

    def fazer_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo

    def fazer_saque(self, valor):
        self.__saldo -= valor
        return self.__saldo