from models import Pessoa,limpar

def main():
    usuario = Pessoa(nome="",idade=0,altura=0.0)
    limpar()
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.idade = int(input("Informe a idade: ").replace(",","."))
    usuario.altura = float(input("Informe a altura: ").replace(",","."))

    print(usuario)
    #print(len(self))
    del(usuario)

if __name__ == "__main__":
    main()