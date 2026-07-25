#TODO - atividade 02
"""
Prog. que recebe a idade e o nome do usuário. E, em seguida mostra o filme em cartaz em 05 sala de cinema:
A volta dos que não foram (livre);
A roda quadrada (12 anos);
As ranças do rei careca (14 anos);
Poeira em alto mar (16 anos);
A vingança do frango assado (16 anos).
O usuário irá escolher a sala onde o filme deeja está passando. Caso o usuário não tenha idade, o programa  impede a sua entrada e re-exeibe  a lista para que o mesmo possa escolhe outro filme.
Caso o usuário tenha a idade mínima, o programa grava em arquivo o bilhete do filme e encerra o programa.
"""
import os

print("Cinema Python")
sala01 = "1 - A volta dos que não foram (livre)"
sala02 = "2 - A roda quadrada (12 anos)"
sala03 = "3 - As tranças do rei careca (14 anos)"
sala04 = "4 - Poeira em alto mar (16 anos)"
sala05 = "5 - A vingança do frango assado (18 anos)"

print(sala01)
print(sala02)
print(sala03)
print(sala04)
print(sala05)

nome = input("Entre com o nome do cliente: ")
idade = int(input("entre com a idade do cliente: "))

opcao = int(input("entre com a sala deseja: "))
bilhete = (f"O {nome} tem {idade} anos e escolheu a sala {opcao}")
#print(bilhete)
nome_arquivo = nome

match opcao:
    case 1:
        print("Divirta-se!")
        with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as s:
        #with open(f"17_arquivos/arquivos/{nome_aquivo}.txt", "w", encoding="utf-8") as f:
            s.write(bilhete)
            print(bilhete)
        print("Texto gravado com sucesso.")
    case 2:
        if idade < 12:
            print("O filme é para maiores de 12 anos.")
        else:
            with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as s:
                s.write(bilhete)
                print(bilhete)
                print("Bom filme.")
            print("Texto gravado com sucesso.")       
    case 3:
        if idade < 14:
            print("O filme é para maiores de 14 anos.")
        else:
            with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as s:
                s.write(bilhete)
                print("Boa diversão.")
    case 4: 
        if idade < 16:
            print("O filme é para maiores de 16 anos.")
        else:
            with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as s:
                s.write(bilhete)
                print("Boa escolha.")
    case 5:
        if idade < 18:
            print("O filme é para maiores de 18 anos.")
        else:
            with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as s:
                s.write(bilhete)
                print("Sencaional.")
    case "_":
        print("Opção inválida.")
