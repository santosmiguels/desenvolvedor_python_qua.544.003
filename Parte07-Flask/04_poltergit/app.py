from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods = ['GET', 'POST'])
def index():
    nome = 'teste 15/09/2026'
    return render_template('index.html', nomeusuario=nome)
if __name__ == "__main__":
    app.run(debug=True)