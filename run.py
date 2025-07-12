import os
from flask import Flask, render_template, url_for, redirect, flash, session, request
from config import db, senha
from app.models.models import Usuario, Curso

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

@app.route('/novocurso')
def novocurso():
    return render_template('novocurso.html', titulo='Adicionar Novo Curso')

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
    
@app.route('/criarcurso', methods=['POST'])
def criarcurso():
    nome = request.form['nome']
    carga = request.form['carga']
    turno = request.form['turno']
    curso = Curso(nome, carga, turno)
    if not nome or not carga or not turno:
        flash('Todos os campos são obrigatórios!')
        return redirect(url_for('novocurso'))
    else:
        db.session.add(curso)
        db.session.commit()
        flash('Curso criado com sucesso!')
    return redirect(url_for('index'))

def home():
    return render_template('index.html', titulo='Inicio')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)