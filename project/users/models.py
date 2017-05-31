from project import db, bcrypt
from flask_login import UserMixin
import geocoder


FollowersFollowee = db.Table('follows',
                              db.Column('id',
                                        db.Integer,
                                        primary_key=True),
                              db.Column('followee_id',
                                        db.Integer,
                                        db.ForeignKey('users.id', ondelete="cascade")),
                              db.Column('follower_id',
                                        db.Integer,
                                        db.ForeignKey('users.id', ondelete="cascade")),
                              db.CheckConstraint('follower_id != followee_id', name="no_self_follow"))

# Likes = db.Table('likes',
#                               db.Column('id',
#                                         db.Integer,
#                                         primary_key=True),
#                               db.Column('msg_id',
#                                         db.Integer,
#                                         db.ForeignKey('messages.id', ondelete="cascade")),
#                               db.Column('user_id',
#                                         db.Integer,
#                                         db.ForeignKey('users.id', ondelete="cascade"))
#                               )

class User(db.Model, UserMixin):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text, unique=True)
  email = db.Column(db.Text, unique=True)
  name = db.Column(db.Text)
  password = db.Column(db.Text)
  image_url = db.Column(db.Text)
  address = db.Column(db.Text)
  city = db.Column(db.Text)
  state = db.Column(db.Text)
  zipcode = db.Column(db.Text)
  latitude = db.Column(db.Text)
  longitude = db.Column(db.Text)
  parties = db.relationship('Party', backref='host',foreign_keys="Party.host_id", lazy='dynamic')
  # followers = db.relationship("User",
  #                             secondary=FollowersFollowee,
  #                             primaryjoin=(FollowersFollowee.c.follower_id == id),
  #                             secondaryjoin=(FollowersFollowee.c.followee_id == id),
  #                             backref=db.backref('following', lazy='dynamic'),
  #                             lazy='dynamic')

  def __init__(self, email, username, name, address, city, state, zipcode, password, image_url=''):
    self.email = email
    self.username = username
    self.name = name
    self.address = address
    self.city = city
    self.state = state
    self.zipcode = zipcode
    self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
    self.image_url = image_url
    g = geocoder.google("{},{},{},{}".format(address, city, state, zipcode))
    [self.latitude, self.longitude] = g.latlng

  def __repr__(self):
    return "#{}: email: {} - username: {}".format(self.id, self.email, self.username)

  def is_followed_by(self, user):
    return bool(self.followers.filter_by(id=user.id).first())

  def is_following(self, user):
    return bool(self.following.filter_by(id=user.id).first())
