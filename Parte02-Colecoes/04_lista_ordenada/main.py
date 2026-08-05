#Lista ordenada
nomes = ["Maria", "Antonio", "Luiz", "Jose", "Ana"]

nomes.sort()
nomes.sort(reverse=True)


for nome in nomes:
    print(nome)


import funcoes_matematicas 
#Programa principal
base = int(input("Entre com o valor da base do quadrilátero: "))
altura = int(input("entre com o valor da altura do quadrilátero: "))
print(funcoes_matematicas.area_quadrilatero(base, altura))

n = int(input("Entre com o número para calcular o fatorial: "))
print(f"O fatorial de {n} é {funcoes_matematicas.fatorial(n)}.")

numero_gera = input("Digite o valor para gerar números pares: ")
(funcoes_matematicas.gerar_pares(numero_gera))
print(numero_gera)