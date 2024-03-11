from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Inicialize a Flask app and sqllite database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd891e1593c0fd3bd1fc82ad93fbb184b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category= 'info'

from myapp import routes