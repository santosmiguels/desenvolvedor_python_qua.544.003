usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

#Usuario dev informa a chave que deseja alterar:

chave = input("Informe o nome da chave: ").strip().lower()

#TODO - verificar se a chave existe
usuario['chave'] = input(f"Entre com a {usuario.get('idade')}: ").strip()

usuario['idade']