#Importação da bibliotecas do sistema:
from flask import Flask, render_template, request
import pyautogui as auto
from datetime import date
import webview
from datetime import date
import os 
import sys

#Início:
if getattr("sys", 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app =Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    nome = 'teste 15/09/2026'
    return render_template('index.html', nomeusuario=nome)

#designer partner MVC 
@app.route("/commitar", methods = ['GET', 'POST'])    
def commitar():
    hoje =  date.today().strftime("%d/%m/%y")
    #mensagem = None
    repositorio = None
    if request.method == "POST":
        repositorio = request.form.get("repositorio", "")
    if repositorio:
        auto.PAUSE = 0.5
        auto.hotkey("win", "r")
        auto.write("cmd")
        auto.press("enter")
        auto.write(f"cd {repositorio}")
        auto.press("enter")
        auto.write("git add .")
        auto.press("enter")
        auto.write(f'git commit -m "Commit do dia {hoje}"')
        auto.press("enter")
        auto.write("git push")
        auto.press("enter")
        #auto.sleep(4)
        auto.press("exit")
        #auto.sleep(2)
        auto.press("enter")
    return render_template('index.html', datahoje = hoje)

if __name__ == "__main__":
    #app.run(debug=True)
    window = webview.create_window(
        title="PolterGit",
        url=app,
        width=600,
        height=300
    )
    webview.start()