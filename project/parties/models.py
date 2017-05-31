from project import db 
from datetime import datetime

class Party(db.Model):
  
  __tablename__ = 'parties'

  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text)
  instructions = db.Column(db.Text)
  date = db.Column(db.DATE)
  time = db.Column(db.TIME)
  cost = db.Column(db.Numeric)
  host_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
  attendee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  # host_rating = db.Column(db.Integer)
  # attendee_rating = db.Column(db.Integer)

  def __init__(self, description, host_id, cost, date, time, instructions=""):
    self.description = description
    self.host_id = host_id
    self.cost = cost
    self.date = date
    self.time = time
    self.instructions = instructions

  def __repr__(self):
    return "{} -{}".format(self.description, self.host_id)