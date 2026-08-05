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
			print(i)
			yield i
	
"""
#algoritmo principal
n = int(input("Entre com o número inteiro positivo: "))
for par in gerar_pares(n):
	print(par)

#programa principal

base = int(input("Entre com o valor da base do quadrilátero: "))
altura = int(input("entre com o valor da altura do quadrilátero: "))
print(area_quadrilatero(base, altura))
"""
