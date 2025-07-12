import string
import random
from flask_sqlalchemy import SQLAlchemy

tamanho = 10
caracteres = string.ascii_letters + string.digits

senha = ''.join(random.choices(caracteres, k=tamanho))

db = SQLAlchemy()