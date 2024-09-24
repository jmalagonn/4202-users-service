from enum import Enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(128))
  password = db.Column(db.String(128))
  user_type = db.Column(db.Integer)
   

class UsuerSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = User
    load_instance = True
    
    
class UserType(Enum):
  CLIENT = 0
  CLIENT_USER = 1