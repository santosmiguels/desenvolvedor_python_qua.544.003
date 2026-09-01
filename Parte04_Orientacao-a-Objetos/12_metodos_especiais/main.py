import models

def main():
    usuario = models.Pessoa(nome="",idade=0,altura=0.0)
    models.limpar()
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.idade = int(input("Informe a idade: ").replace(",","."))
    usuario.altura = float(input("Informe a altura: ").replace(",","."))

    print(usuario)
    #print(len(self))
    #del(usuario)
    #delete(usuario)

if __name__ == "__main__":
    main()