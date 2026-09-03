#Automação com Python. Dia 02/09/2026.
#Bibliotecas para automação: Selenium e Pyautogui.

import pyautogui as auto
import os
#import time


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def ir_pesquisar():
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")
    auto.press("tab")


def main():
    auto.PAUSE = 0.75
    auto.press("win")
    auto.write("firefox")
    auto.press("enter")
    #auto.PAUSE = 2
    auto.write("youtube.com.br")
    auto.press("enter")
    auto.sleep(5)
    #auto.press("/")
    ir_pesquisar()
    auto.write("python")
    auto.press("enter")
    auto.sleep(3)
    auto.hotkey("ctrl","t")
    auto.write("python.org")
    auto.press("enter")


if __name__ == "__main__":
    main()