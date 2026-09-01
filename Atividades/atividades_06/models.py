#Criação das classes e interfaces:
import os
from abc import ABC,abstractclassmethod

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#Interfaces
class Iconta(ABC):
    @abstractclassmethod
    def consultar_dados():
        pass

    @abstractclassmethod
    def gerar_extrato():
        pass

    @abstractclassmethod
    def depositar(valor):
        pass

    def sacar(valor):
        pass

#Classes:

class Conta(Iconta):
    def __init__(self,agencia,n_conta,saldo,pessoa):
        #super().__init__()
        #self.__titular = titular
        #self.__cpf = cpf
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo
        self.__pessoa = pessoa

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self,agencia):
        self.__agencia = agencia

    @property
    def n_conta(self):
        return self.__n_conta

    @n_conta.setter
    def n_conta(self,n_conta):
        self.__n_conta = n_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    @property
    def pessoa(self):
        return self.__pessoa

    @pessoa.setter
    def pessoa(self,pessoa):
        self.__pessoa = pessoa

    def consultar_dados(self):
        print(f"Nome do titular da conta: {self.__nome}.")
        print(f"Número do CPF do titular: {self.__cpf}.")
        print(f"Número da agência: {self.__agencia}.")
        print(f"Número da conta: {self.__n_conta}.")
        print(f"Saldo da conta: {self.__saldo}.")

    def gerar_extrato(self):
        pass

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor
        return self.saldo


class Pessoa:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
        #self.__conta = conta

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cp = cpf
    """
    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self,conta):
        self.__conta = conta
    """
    def __str__(self):
        return f"O titular da contar é {self.__nome} e tem o CPF: {self.__cpf}."