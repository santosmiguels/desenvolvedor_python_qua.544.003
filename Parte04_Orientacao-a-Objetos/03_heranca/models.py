
#Criação da classes:
class Pessoa:
    def __init__(self, email, telefone, endereco):
        self.email = email
        self.telefone = telefone
        self.enderecp = endereco

    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"endereco: {self.endereco}")

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, email, telefone, endereco):
        super().__init__(email, telefone, endereco)
        self.nome = nome
        self.cpf = cpf

    #def exibir_dados_usuario(self):
     #   print(f"nome: {self.nome}")
      #  print(f"cpf: {self.cpf}")
       # return super().exibir_dados()

    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"cpf: {self.cpf}")
        super().exibir_dados()    

class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, nome_fantasia, cnpj, email, telefone, endereco):
        super().__init__(email, telefone, endereco)
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj =cnpj

    def exibir_dados(self):
        print(f"razao_social: {self.razao_social}")
        print(f"nome_fantasia: {self.nome_fantasia}")
        print(f"cnpj: {self.cnpj}")
        super().exibir_dados() 


