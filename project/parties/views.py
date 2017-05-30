from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.parties.models import Party
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps
from IPython import embed
import json

parties_blueprint = Blueprint(
  'parties',
  __name__,
  # template_folder='templates'
)