from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0202@localhost:5432/mixxyedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

# MODELOS


class user(database.Model):
    __tablename__ = 'usuarios'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    password = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(80), nullable=False)

    # crear mas relaciones

    def __repr__(self):
        return f'usuario: id={self.id}, user={self.user}, email={self.email}'

# crear mas modelos

database.create_all()

# register - login - home

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/<string:perfil>')
def home(perfil):
    return render_template("home.html", perfil=perfil)

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
        except Exception as e:
            database.session.rollback()
            print(sys.exc_info())
        finally:
            database.session.close()

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login_user():
    if request.method == 'POST':
        verificador = ""
        id_user = ""

        email = request.form.get('email')
        password = request.form.get('password')

        users_passwords = user.query.filter_by(email='{}'.format(email))

        for pswd in users_passwords:
            if (check_password_hash(pswd.password, password) and email==pswd.email):
                verificador = pswd.username
                id_user = pswd.id
                break
        
        if verificador!="":
            return redirect(url_for('home', perfil=verificador))
        else:
            return redirect(url_for('login'))

if __name__ == '__main__' :
    app.run(port=3000, debug=True)