#Importar biblioteca
import os

os.system("cls" if os.name == "nt" else "clear")
# lista vazia
nomes = []

while True:
    nome = input("Informe um nome: ").strip().title()
    #inserir nome na lista:
    nomes.append(nome)
    opcao = input("Deseja inserir novo nome? (s/n)")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "s":
            continue
        case _:
            break

print("Lista de nomes:\n")
for i, nome in enumerate(nomes, start=1):
    print(nome)

"""
#lambda
def area_quadrilatero(b,h):
    area = b * h
    return area


#programa principal
base = int(input("Entre com o valor da base do quadrilátero: "))
altura = int(input("entre com o valor da altura do quadrilátero: "))
print(area_quadrilatero(base, altura))
"""