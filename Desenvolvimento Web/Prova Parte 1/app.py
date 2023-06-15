from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'senha'

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/newsletter")
def newsletter():
    return render_template("newsletter.html")


@app.route("/inscrever", methods=["POST"])
def inscrever():
    nome = request.form.get("nome")
    email = request.form.get("email")
    tel = request.form.get("tel")

    if 'usuarios' not in session:
        session['usuarios'] = {}

    usuarios = session['usuarios']
    if email in usuarios:
        return 'Usuário já cadastrado com este e-mail.'

    usuarios[email] = {'nome': nome, 'email': email, 'tel': tel}
    session['usuarios'] = usuarios

    return render_template("confirma.html", nome=nome, email=email, tel=tel)

if __name__ == "__main__":
    app.run(debug=True)
