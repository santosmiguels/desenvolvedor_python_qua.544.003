import os

os.system("cls" if os.name == "nt" else "clear")

somar = lambda x,y : x+y

def main():
    x = int(input("informe o valor de x: "))
    y = int(input("Informe o valor de y: "))

    print(f"O valor da soma é {somar(x, y)}.")

if __name__ == "__main__":
    main()