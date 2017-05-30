from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, InputRequired

class LoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[Length(min=6)])


class UserForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  email = StringField('email', validators=[DataRequired(), Email()])
  name = StringField('name', validators=[DataRequired()])
  password = PasswordField('password', validators=[Length(min=6)])
  image_url = StringField('image_url')
  address = StringField('address', validators=[InputRequired()])
  city = StringField('city', validators=[InputRequired()])
  state = StringField('state', validators=[InputRequired()])
  zipcode = StringField('zipcode', validators=[InputRequired()])
  # latitude = StringField('latitude')
  # longitude = StringField('longitude')

class UserEditForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  email = StringField('email', validators=[DataRequired(), Email()])
  name = StringField('name', validators=[DataRequired()])
  password = PasswordField('password', validators=[Length(min=6)])
  image_url = StringField('image_url')
  address = StringField('address', validators=[InputRequired()])
  city = StringField('city', validators=[InputRequired()])
  state = StringField('state', validators=[InputRequired()])
  zipcode = StringField('zipcode', validators=[InputRequired()])
  latitude = StringField('latitude')
  longitude = StringField('longitude')