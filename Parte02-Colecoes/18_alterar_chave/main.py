usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

#Usuario dev informa a chave que deseja alterar:

chave = input("Informe o nome da chave: ").strip().lower()

if chave in usuario:
    usuario[chave] = input(f"Entre com o novo valor para {chave}.").strip()

    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print("Chave não encontrada.")