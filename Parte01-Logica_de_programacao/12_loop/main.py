#declaração de variaveis
try:
    #TODO - 
    n = int(input("informe um valor inteiro: "))
    while n >= 0: 
        print(n)
        n -= 1
except:
    print("Não foi possível exibir a contagem.")