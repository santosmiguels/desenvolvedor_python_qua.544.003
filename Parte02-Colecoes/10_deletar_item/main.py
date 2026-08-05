nomes = ["Maria", "Antonio", "Luiz", "Jose", "Ana", "Esmeralda", "João", "Marieta"]

nome = input("Informe o nome que deseja exluir: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)
    print(f"O indice do nome {nome} na lista é {indice}." )
    del(nomes[indice]) #= input("Informe o novo nome: ").strip().title()
    print("Nome excluido com sucesso.")
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado")