import models

def main():
    departamento = models.Departamento(nome="")
    empresa = models.Empresa(nome="", departamento=departamento)

    models.limpar()

    empresa.nome = input("Informe o nome da empresa: ")
    empresa.departamento.nome = input("Informe o nome do departamento: ")

    models.limpar()

    print(empresa.detalhes())

if __name__ == "__main__":
    main()