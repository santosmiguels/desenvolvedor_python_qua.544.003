usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

print("\n")
print(f"nome: {usuario['nome']}.")
print(f"idade: {usuario['idade']}.")
print(f"email: {usuario['email']}.")
print(f"cpf: {usuario['cpf']}.")

print("\n")
print(f"nome: {usuario.get('nome')}.")
print(f"idade: {usuario.get('idade')}.")
print(f"email: {usuario.get('email')}.")
print(f"cpf: {usuario.get('cpf')}.")

print("\n")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")