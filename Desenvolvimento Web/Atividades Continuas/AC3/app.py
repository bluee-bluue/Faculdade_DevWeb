from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/confirmacao', methods=['GET', 'POST'])
def confirmacao():
    nome = request.form['nome']
    email = request.form['email']
    return render_template('confirmacao.html', nome=nome, email=email)


if __name__ == '__main__':
    app.run(debug=True)

