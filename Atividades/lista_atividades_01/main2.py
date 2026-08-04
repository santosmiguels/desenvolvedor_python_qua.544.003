lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1.append(11)
lista1.insert(11, 12)#lista1.remove(11)
lista1.pop()
lista1.remove(1)
del lista1[0]

print(type(lista1))
print(type(lista1[0]))
for i in range(len(lista1)):
    if i < len(lista1):
        print(f"{i} - {lista1[i]}, {type(lista1[1])}")
    i += i
lista_compras = ["arroz", "feijão", "milho", "café", "leite", "açuca", "ovos", "macarrão", "carne"]
for i in range(len(lista_compras)):
    if i < len(lista_compras):
        print(f"{i} - {lista_compras[i]}, {type(lista_compras[i])}")
    i += i
lista2 = lista1 + lista_compras
print(lista2)
#print(lista_compras)
#print(len(lista1)