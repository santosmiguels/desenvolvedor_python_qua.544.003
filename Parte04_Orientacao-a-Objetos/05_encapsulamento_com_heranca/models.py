import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

class Pessoa:
    def __init__(self, email, telefone):
        self.__email = email
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @property
    def telefone(self):
        return self.__telefone

    @email.setter
    def email(self, email):
        self.__email = email

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, email, telefone):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(email=email, telefone=telefone)

    @property
    def nome(self):
        return  self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, email, telefone):
        self.__nome_fanasia = nome_fantasia
        self.__cnpj = cnpj

    @property
    def nome_fantasia(self):
        return self.__nome_fanasia

    @property
    def cnpj(self):
        return self.__cnpj

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fanasia = nome_fantasia

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj