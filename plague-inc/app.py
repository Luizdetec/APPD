from flask import Flask, render_template, request, send_from_directory
import calc

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template('menu.html')


def get_image(filename):
    return send_from_directory('static/imagens', filename)


@app.route('/h1n1')
def h1n1():
    calc.calculo("h1n1","C:\Plague\plague-inc\static\imagens\h1n1.png")
    return render_template('h1n1.html')


@app.route('/covid')
def covid():
    calc.calculo("covid","C:\Plague\plague-inc\static\imagens\covid.png")
    return render_template('covid.html')


@app.route('/gripe')
def gripe():
    calc.calculo("gripe", "C:\Plague\plague-inc\static\imagens\gripe.png")
    return render_template('gripe.html')


@app.route('/doenca_nova', methods=["GET", "POST"])
def doenca_nova():
    beta = 0
    gamma = 0
    tempo = 0
    nome_doenca = ""
    lista_historico = []
    if request.method == "POST":
        if request.form.get("beta") and request.form.get("gamma") and request.form.get("tempo") and request.form.get("nome_doenca"):
            nome_doenca = request.form.get("nome_doenca")
            beta = float(request.form.get("beta"))
            gamma = float(request.form.get("gamma"))
            tempo = int(request.form.get("tempo"))
            calc.nova_doenca(beta, gamma, tempo, nome_doenca)
            lista_historico = calc.historico()
    return render_template('doenca_nova.html', beta=beta, gamma=gamma, tempo=tempo, nome_doenca=nome_doenca, lista_historico=lista_historico)


app.run(debug=True)