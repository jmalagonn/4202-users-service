from datetime import timedelta
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models import db, User
from models.models import UserType 

class UserView(Resource):
  
  def get(self, username):
    
    user = User.query.filter_by(username = username).scalar()
    
    if user is None:
      return False, 404
    else:
      return { "username": user.username, "user_type": user.user_type }
  
  def post(self): 
    
    new_user = User(
      username = request.json['username'],
      password = request.json['password'],
      user_type = UserType.CLIENT.value if request.json['user_type'] == UserType.CLIENT.value else UserType.CLIENT_USER.value
    )
    
    try:
      db.session.add(new_user)
      db.session.commit()
      
      return True, 200
    except:
      return False, 200
    
  def delete(self, username):
    user = User.query.filter_by(username = username).first()
    
    if user is None:
      return False, 404
    
    try:
      db.session.delete(user)
      db.session.commit()
      
      return True, 200
    except:
      return False, 200
    
class LoginView(Resource):
    
 def post(self):

    user = User.query.filter_by(username = request.json['username'], password = request.json['password']).scalar()

    if user is None:
      return False, 404
    else:
        token_de_acceso = create_access_token(
            identity={
                "id": user.id,
                "username": user.username,
                "user_type": user.user_type
            },
            expires_delta=timedelta(days=1),
        )
        
        return {"username": user.username, "token": token_de_acceso}
    