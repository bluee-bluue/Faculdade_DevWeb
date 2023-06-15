from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'suasenha'

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    if 'usuarios' not in session:
        session['usuarios'] = {}

    usuarios = session['usuarios']
    if email in usuarios:
        return 'Usuário já cadastrado com este e-mail.'

    usuarios[email] = {'nome': nome, 'email': email, 'senha': senha}
    session['usuarios'] = usuarios

    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']

    if 'usuarios' in session:
        usuarios = session['usuarios']
        if email in usuarios and usuarios[email]['senha'] == senha:
            session['sessoes'] = {}
            sessoes = session['sessoes']
            sessao_id = len(sessoes) + 1
            sessoes[sessao_id] = email
            session['sessoes'] = sessoes

            response = redirect('/area_logada')
            response.set_cookie('sessao_id', str(sessao_id))
            session['usuario_logado'] = email
            return render_template('area_logada.html')

    return 'Usuário ou senha inválidos.'

@app.route('/area_logada')
def area_logada():
    if 'sessoes' in session and 'sessao_id' in request.cookies:
        sessoes = session['sessoes']
        sessao_id = int(request.cookies['sessao_id'])

        if sessao_id in sessoes:
            return render_template('area_logada.html')

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.pop('sessoes', None)
        response = redirect('/login')
        response.delete_cookie('sessao_id')
        return response

    return redirect('/login')


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

