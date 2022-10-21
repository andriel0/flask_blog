from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuarios = ['andriel', 'alexandre', 'oliveira']


@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)