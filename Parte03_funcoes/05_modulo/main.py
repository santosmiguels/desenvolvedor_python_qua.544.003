import modulo

modulo.limpar_tela()
a = float(input("Informe o valor de 'a': ").replace(",", "."))
b = float(input("Informe o valor de 'b': ").replace(",", "."))
print(f"A valor da equacao do rimeiro grau é: {modulo.equacao_primeiro_grau(a, b)}")