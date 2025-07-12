from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(50), nullable=False)
    funcao = db.Column(db.String(50), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)
    
    def __init__(self, nome, email, senha, funcao):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.funcao = funcao
        self.ativo = True

class Curso(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)
    turno = db.Column(db.String, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, nome, carga_horaria, turno):
        
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.turno = turno
        self.ativo = True
