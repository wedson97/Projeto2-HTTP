from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('agenda.json', 'r') as ler:
        contatos = json.load(ler)
    return render_template('contatos.html', contatos=contatos)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        with open('agenda.json', 'r') as ler:
          contatos = json.load(ler)

        nome = request.form.get('nome')
        email = request.form.get('email')
        novoContato = {'nome': nome, 'email': email}
        contatos.append(novoContato)

        with open('agenda.json', 'w') as salvar:
            json.dump(contatos, salvar, indent=2)
          
    return render_template("cadastrar.html")


app.run(host='0.0.0.0', port=81)
