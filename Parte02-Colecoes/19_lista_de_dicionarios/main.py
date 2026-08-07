usuarios = [
    {
        'nome': "Fulano de Tal",
        'idade': 35,
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Cicrano de Tal",
        'idade': 30,
        'email': "cicrano@gmail.com"
    },
    {
        'nome': "Teste de Tal",
        'idade': 40,
        'email': "teste@gmail.com",
    }
]
#print(usuarios)
for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")