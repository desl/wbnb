from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, Email, Length, InputRequired, NumberRange
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField

class PartyForm(FlaskForm):
  description = StringField('Description', validators=[DataRequired()])
  instructions = StringField('Instructions')
  date = DateField('Date')
  time = TimeField('Start Time')
  cost = StringField('Cost $', validators=[DataRequired()])
  # host_id = StringField('host', validators=[InputRequired()])
  # attendee = StringField('attendee')

class JoinForm(FlaskForm):
  party_id = StringField('Party ID')
  verb = StringField('verb',validators=[DataRequired()])
  lat = StringField('lat')
  lng = StringField('lng')