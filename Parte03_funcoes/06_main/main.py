#Calcular se o usuário é maior de idade:

import modulo as m

def main ():
    m.limpar_tela()
    
    usuario = input("Digite o nome do usuário: ").strip().title()
    idade = int(input("Digite a idade do usuário: "))

    print(f"O {usuario} tem {idade} e é {m.maior_idade(idade)}.")

if __name__ == "__main__":
    main()