from flask import render_template, request, flash, redirect, url_for
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora import app


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