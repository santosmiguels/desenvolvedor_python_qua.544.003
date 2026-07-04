#Importação de biblioteca
import os
import time

#Tratamento de execeção
try:
    #entrada de dados
    n = int(input("Informe um número interio: "))
    #Limpa a tela
    os.system("cls" if os.name == "nt" else "clear")
    #Contagem
    while n >=0:
        print(f"{n}...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        n -= 1
    print("Booommm!!!!!!!!! 💕")
except Exception as e:
    print("Não foi possível iniciar a contagem. {e}")
