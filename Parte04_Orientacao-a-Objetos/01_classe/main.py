#Criar classes
class Pessoa:
    #Metodo construtor
    def __init__(self, nome, idade, email, altura):
        #Atributos da classe Pessoa:
        self.nome = nome
        self.idade = idade
        self.email = email
        self.altura = altura

    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"email: {self.email}")
        print(f"altura: {self.altura}")

#Programa principal:
def main():
    usuario = Pessoa(nome="", idade=0, email="", altura=0.0)

    usuario.nome = input("Informe o nome do usuário: ")
    usuario.idade = int(input("Informe a idade do usuário: "))
    usuario.email = input("Informe o email do usuário: ")
    usuario.altura = float(input("Informe a altura do usuário: ").replace(",", "."))

    usuario.exibir_dados()

if __name__ == "__main__":
    main()