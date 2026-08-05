cidades = ["Brasilia",
           "Rio de Janeiro",
           "São Paulo",
           "Belo Horizonte",
           "Goiania",
           "Manaus",
           "Fortaleza",
           "Florianópolis"
           ]

cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

print(f"A cidade {cidade_pesquisada} está na lista." if cidade_pesquisada in cidades else f"Cidade não encontrada.")
