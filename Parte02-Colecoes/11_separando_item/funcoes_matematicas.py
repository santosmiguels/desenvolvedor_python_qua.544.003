#lambda ver como fazer
# Calcular a área de um quadrilátero:
def area_quadrilatero(b,h):
    area = b * h
    return area

#Calcular o fatorial
def fatorial(n):
    return 1 if n==0 else n * fatorial(n-1)

#Programa principal
#n = int(input("Entre com o número para clacular o fatorial: "))
#print(f"O fatorial {n} é {fatorial(n)}.")

def gerar_pares(n):
	#Gerar os número pares de o até n-1.
	for i in range(n):
		if i % 2 == 0:
			#print(i)
			yield i

#Classe
class Pessoa:
	def __init__(self, nome, idade, altura):
		self.nome = nome
		self.idade = idade
		self.altura = altura

	#Método da classe
	def exibir_dados(self):
		print(f"Nome: {self.nome}.")
		print(f"Idade: {self.idade}.")
		print(f"Altura: {self.altura}.")


def main():
	#Instacia a classe Pessoa:

	usuario = Pessoa(nome="", idade=0, altura=0.0)
	usuario.nome = input("Entre com o nome: ")
	usuario.idade = int(input("Entre com a idade: "))
	usuario.altura = float(input("Entre a altura: "))

	usuario.exibir_dados()



"""
class Pessoa:
	nome = "alex"
	idade = 39
	cargo = "Programador"
	email = "alex@gmail.com"

	#Método da classe
	def apresentar(self):
		print(f"Olá, menu nome é {self.nome}, tenho {self.idade} anos, trabalho como {self.cargo}, e meu e-mail é {self.email}")

#algoritmo principal
n = int(input("Entre com o número inteiro positivo: "))
for par in gerar_pares(n):
	print(par)

#programa principal

base = int(input("Entre com o valor da base do quadrilátero: "))
altura = int(input("entre com o valor da altura do quadrilátero: "))
print(area_quadrilatero(base, altura))
"""
