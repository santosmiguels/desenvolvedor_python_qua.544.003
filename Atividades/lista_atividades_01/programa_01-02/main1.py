#definição de função:
def gerar_pares(n):
    """Gera os número pares de 0 até n-1"""
    for i in range(n):
        if i % 2 == 0:
            yield i

#algoritmo principal
numero_par = int(input())
for par in gerar_pares(numero_par):
    print(par)


"""
def calcular_equacao_primeiro_grau (a, b):
    x = -b/a
    return x

a = int(input("Informe o valor de a: "))
b = int(input("informe o valro de b: "))

print(f"O valor de x na equação do primeiro graus é {calcular_equacao_primeiro_grau(a, b)}")

def exibir_msg ():
    print("-"*10, "Bem vindo ao SENAI", "-"*10)
    print("Você está fazendo o cursos Desenvolvedor Python.")

#Programa principal:
descisão = input("Deseja imprimir a mensagem? (s/n)")
match descisão:
    case "s":
        exibir_msg()
    case "n":
        pass
    case _:
        print("Resposta inválida")

lista = []

while True:
    nome = input("Entre com o nome: ")
    idade = input("Entre com a idade: ")
    profissao = input("Entre com a profissão: ")

    dicionario = {"cliente": nome,
                "idade_cliente": idade,
                    "profissao_cliente": profissao }

    print(dicionario)
    lista.append(dicionario)
    print(lista)

    continua =  input("Deseja continuar: (s/n).")

    if continua == "s":
        continue
    else:
        break


lista =["Maria", "João", "Antonio"]
tupla1 = ("José", "Pedro", "Luiz", "Mauro")
separador = ", "

nomes = separador.join(tupla1)
print(nomes)

dic = {"nome": "Maria",
       "idade": 40,
       "profissao": "Programador"}

dic["cidade"] = input("Entre com a cidade: ")

print(dic)
print(dic["nome"])
print(dic.get("idade"))

dic.pop(input("Informe a chave a ser excluida: "), None)
print(dic)

del dic[input("Qual é a chave a ser removida: ")]
print(dic)



lista.insert(3, "Alex")
#tupla1[1] = "Mauro"
print(lista)

del(lista[0])
print (lista)

for pessoa in tupla1:
    print(pessoa)

nome = input("Pesquisar: ").strip()
if nome in tupla1:
    print(nome)
else:
    print(f"{nome} não encontrado")

#quantidade = lista.count(nome_pessoas)
"""