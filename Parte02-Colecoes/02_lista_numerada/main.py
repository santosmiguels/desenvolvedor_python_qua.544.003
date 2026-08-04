frutas = ["Maça", "Abacaxi", "Morango", "Maracuja"]

for i,fruta in enumerate(frutas, start=1):
    print(f"Fruta {i}: {fruta}")

"""
def fatorial(n):
    return 1 if n==0 else n * fatorial(n-1)

#Programa principal
n = int(input("Entre com o número para clacular o fatorial: "))
print(f"O fatorial {n} é {fatorial(n)}.")

def gerar_pares(n):
	#Gerar os número pares de o até n-1.
	for i in range(n):
		if i % 2 == 0:
			yield i
			

#algoritmo principal
n = int(input("Entre com o número inteiro positivo: "))
for par in gerar_pares(n):
	print(par)
"""