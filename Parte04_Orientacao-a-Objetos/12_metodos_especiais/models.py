import os

def limpar():
    os.system("cls" if os.name == "nt" else "Clear")

class Pessoa:
    #construtor:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        #return f"Olá, menu nome é {self.nome}, {self.idade}."
        return f"Olá, meu nome é {self.nome}, tenho {len(self)} anos de idade e {float(self)} metros de altura."

    def __len__(self):
        return self.idade

    def __float__(self):
        return self.altura

    del __del__(self):
    print(f"Objeto {self} destruído com sucesso.")

    

