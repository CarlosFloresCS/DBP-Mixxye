from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from werkzeug.utils import redirect
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:n4nd0p3@localhost:5432/mixxyedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

migrate= Migrate(app,database) 

class user(database.Model):
    __tablename__ = 'usuarios'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    password = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(80), nullable=False)

    musics_user = database.relationship('music', backref='musics_user', cascade="all,delete-orphan")

    def __repr__(self):
        return f'usuario: email={self.email}'


"""class playlist(database.Model):
    __tablename__= 'listas'
    id = database.Column(database.Integer, primary_key=True)
    nameL = database.Column(database.String(50), nullable=False)

    musics_playlist = database.relationship('music', backref='musics_playlist', cascade="all,delete-orphan")
    id_U = database.Column(database.Integer,database.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f'listado: nameL={self.nameL}'"""

class music(database.Model):
    __tablename__= 'musicas'
    id = database.Column(database.Integer, primary_key=True)
    nameM = database.Column(database.String(50), nullable=False)
    url = database.Column(database.String(300), nullable=False)

    id_U = database.Column(database.Integer,database.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f'musica: link={self.url}'



database.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/<string:perfil>//<string:id>')
def home(perfil, id):
    return render_template("home.html", perfil=perfil, id=id)

@app.route('/<string:perfil>//<string:id>/biblioteca/')
def biblioteca(perfil, id):
    biblioteca = music.query.filter_by(id_U='{}'.format(id))
    return render_template("biblioteca.html", perfil=perfil, id=id, biblioteca=biblioteca )

@app.route('/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            email = request.form.get('email')
            password = generate_password_hash(request.form.get('password'))
        
            _user_ = user(username=username, password=password, email=email)

            database.session.add(_user_)
            database.session.commit()

            return redirect(url_for('login'))
        except Exception as e:
            database.session.rollback()
            print(sys.exc_info())
        finally:
            database.session.close()

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login_user():
    if request.method == 'POST':
        perfil = ""

        email = request.form.get('email')
        password = request.form.get('password')

        users_passwords = user.query.filter_by(email='{}'.format(email))

        for pswd in users_passwords:
            if (check_password_hash(pswd.password, password) and email==pswd.email):
                perfil = pswd.username
                idU = pswd.id
                break
        
        if perfil!="":
            return redirect(url_for('biblioteca', perfil=perfil, id=idU))
        else:
            return redirect(url_for('login'))

@app.route('/<string:perfil>//<string:id>/add', methods=['POST'])
def agregar_en_biblioteca_user(perfil, id):
    if request.method == 'POST':
        try:
            nameM = request.form.get('nombre')
            url = request.form.get('url')

            msc = music(nameM=nameM, url=url, id_U=id)

            database.session.add(msc)
            database.session.commit()

        except Exception as e:
            database.session.rollback()
            print(sys.exc_info())
        finally:
            database.session.close()
    return redirect(url_for('biblioteca', perfil=perfil, id=id))

@app.route('/<string:perfil>//<string:id>/delete/<string:mid>')
def delete_music(perfil, id, mid):
    database.engine.execute("delete from musicas where id={}".format(mid))
    database.session.commit()
    return redirect(url_for('biblioteca', perfil=perfil, id=id))


if __name__ == '__main__' :
    app.run(port=3000, debug=True)