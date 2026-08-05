cidades = ["Brasilia",
           "Rio de Janeiro",
           "São Paulo",
           "Belo Horizonte",
           "Goiania",
           "Manaus",
           "Fortaleza",
           "Florianópolis"
           ]

cidade = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

if cidade in cidades:
    indice = cidades.index(cidade)
    print(f"O indice da cidade {cidade} na lista é {indice}." )

#print(f"A cidade {cidade_pesquisada} está na lista." if cidade_pesquisada in cidades else f"Cidade não encontrada.")
