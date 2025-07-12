import os
from flask import Flask, render_template, url_for, redirect, flash, session, request
from config import db, senha
from app.models.models import Usuario

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = senha

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'app', 'dados.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', titulo='Inicio')

@app.route('/login')
def login():
    return render_template('login.html', titulo='Login')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    usuario = Usuario.query.filter((Usuario.nome == usuario)).first()

    if usuario and usuario.senha == senha:
        session['Usuario_Logado'] = usuario.nome
        return redirect(url_for('index'))
    else:
        flash('Não foi possivel realizar o login!')
        return redirect(url_for('login'))


def home():
    return render_template('index.html', titulo='Inicio')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)