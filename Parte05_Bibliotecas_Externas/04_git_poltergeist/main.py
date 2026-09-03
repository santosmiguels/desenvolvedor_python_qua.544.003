import pyautogui as auto
from datetime import date

def hoje():
    return date.today().strftime("%d/%m/%y")

def main():
    auto.PAUSE = 0.75
    auto.press("win")
    auto.write("cmd")
    auto.press("Enter")
    #auto.sleep(5)
    #auto.hotkey("ctrl","j")
    #auto.sleep(5)
    #auto.write("cd..")
    auto.write("cd Miguel/desenvolvedor_python_qua.544.003")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "{hoje()}')
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")
    """
    auto.PAUSE = 0.75
    auto.press("win")
    auto.write("vscode")
    auto.press("Enter")
    auto.sleep(5)
    auto.hotkey("ctrl","j")
    auto.sleep(5)
    #auto.write("cd..")
    auto.write("cd Miguel/desenvolvedor_python_qua.544.003")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "{hoje()}')
    auto.press("enter")
    auto.write("git push")
    auto.press("enter")
    """






if __name__ == "__main__":
    main()