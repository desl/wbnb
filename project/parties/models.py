from project import db 
from datetime import datetime

class Party(db.Model):
  
  __tablename__ = 'parties'

  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text)
  instructions = db.Column(db.Text)
  timestamp = db.Column(db.DateTime)
  cost = db.Column(db.Numeric)
  host_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
  attendee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  # host_rating = db.Column(db.Integer)
  # attendee_rating = db.Column(db.Integer)

  def __init__(self, description, host_id, cost, timestamp=datetime.utcnow(), instructions=""):
    self.description = description
    self.host_id = host_id
    self.timestamp = timestamp
    self.cost = cost
    self.instruction = instructions

  def __repr__(self):
    return "{} -{}".format(self.description, self.host_id)