from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
import os
from IPython import embed
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'postgres://localhost/wbnb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or "it's a secret"
# app.config['SQLALCHEMY_ECHO'] = True


# If we are in production, make sure we DO NOT use the debug mode
if os.environ.get('ENV') == 'production':
    debug = False
    # Heroku gives us an environment variable called DATABASE_URL when we add a postgres database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/wbnb'
    app.config['SQLALCHEMY_ECHO'] = True


modus = Modus(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.parties.views import parties_blueprint
from project.users.models import User
from project.parties.models import Party

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(parties_blueprint, url_prefix='/parties/<int:id>')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
def root():
  # if current_user.is_anonymous:
  #   pass
  #   return render_template('home.html')
  # else:
  #   u = User.query.get(current_user.id)
  return render_template('home.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r