nomes = ["Maria", "Antonio", "Luiz", "Jose", "Ana", "Esmeralda", "João", "Marieta"]

nome_antigo = input("Informe o nome que deseja alterar: ").strip().title()

if nome_antigo in nomes:
    indice = nomes.index(nome_antigo)
    print(f"O indice do nome {nome_antigo} na lista é {indice}." )
    nomes[indice] = input("Informe o novo nome: ").strip().title()
    print("Nome alterado com sucesso.")
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado")