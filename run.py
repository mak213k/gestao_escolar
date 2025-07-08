import os
from flask import Flask, render_template, url_for
from config import db
from app.models.models import Usuario

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'app', 'dados.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html', titulo='Inicio')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)