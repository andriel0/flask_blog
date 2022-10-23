from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

lista_usuarios = ['andriel', 'alexandre', 'oliveira']


app.config['SECRET_KEY'] = 'e3af64a50713936d82691a3739ec6bb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'XXXXXXXXXXXXXXXXXX'

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()

    if form_login.validate_on_submit() and 'btn_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criar_conta.validate_on_submit() and 'btn_submit_criar_conta' in request.form:
        flash(f'Conta criada com sucesso no e-mail {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)


if __name__ == '__main__':
    app.run(debug=True)
