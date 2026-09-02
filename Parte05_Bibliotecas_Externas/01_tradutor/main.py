#Bibliotecas externas.
#É importante gerar o requirements
#from deep-translator import GoogleTranslator
#from deep_translator import GoobleTranslator
from deep_translator import GoogleTranslator

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def traduzir(texto):
    tradutor = GoogleTranslator(source="auto",target="pt")
    return tradutor.translate(texto)

def main():
    limpar()
    while True:
        print("0 - Sair do programa.")
        print("1 - Traduzir texto para o português.")
        opcao = input("Entre com a opção desejada: ")
        if opcao == "0":
            break
        elif opcao == "1":
            try:
                texto = input("Informe o texto a ser traduzido: ")
                limpar()
                print(traduzir(texto))
                continue
            except Exception as e:
                print("Não foi possível traduzir. {e}")
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()