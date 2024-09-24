from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(128))
  password = db.Column(db.String(128))
   

class UsuerSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = User
    load_instance = True