usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

#Adiciona a chave telefone no dicionário:
usuario['telefone'] = input(f"Entre com o telefone de {usuario.get('nome')}: ").strip()
usuario['ano'] = input(f"Entre com o ano do {usuario.get('nome')}: ").strip()

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")