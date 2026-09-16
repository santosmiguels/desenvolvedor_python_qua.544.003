from flask import Flask, render_template, request
import pyautogui as auto
from datetime import date

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    nome = 'teste 15/09/2026'
    return render_template('index.html', nomeusuario=nome)

#designer partner MVC 
@app.route("/commitar", methods = ['GET', 'POST'])    
def commitar():
    hoje =  date.today().strftime("%d/%m/%y")
    mensagem = None
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
        auto.write('git commit -m "{{hoje}}"')
        auto.press("enter")
        auto.write("git push")
        auto.press("enter")
    else:
        mensagem = "Repositório inválido."
    return render_template("index.html", msg = mensagem)



    

    return render_template('index.html', datahoje = hoje)

if __name__ == "__main__":
    app.run(debug=True)