from random import randint
from unittest import TestCase
from faker import Faker
from flask import json
from app import app
from models.models import UserType

class TestUser(TestCase):
  def setUp(self):
    self.client = app.test_client()
    self.faker = Faker()
    self.request_headers = {'Content-Type': 'application/json'}
    
  def test_register_user(self):
    
    new_user = {
      'username': self.faker.user_name(),
      'password': self.faker.password(),
      'user_type': UserType.CLIENT.value if randint(0, 9) % 2 == 0 else UserType.CLIENT_USER.value
    }
    
    register_user_request = self.client.post('register', data = json.dumps(new_user), headers = self.request_headers)
    response = register_user_request.get_json()
    
    self.assertEqual(True, response)
    
    delete_user_request = self.client.delete('remove/{}'.format(str(new_user['username'])), headers = self.request_headers)
    response = delete_user_request.get_json()
    
    self.assertEqual(True, response)
    
    
  def test_login_user(self):
    
    new_user = {
      'username': self.faker.user_name(),
      'password': self.faker.password(),
      'user_type': UserType.CLIENT.value if randint(0, 9) % 2 == 0 else UserType.CLIENT_USER.value
    }
    
    register_user_request = self.client.post('register', data = json.dumps(new_user), headers = self.request_headers)
    response = register_user_request.get_json()
    
    self.assertEqual(True, response)
    
    login_request = self.client.post('login', data = json.dumps(new_user), headers = self.request_headers)
    response = login_request.get_json()
    
    self.assertEqual(response['username'], new_user['username'])
    self.assertIsNotNone(response['token'])
    
    delete_user_request = self.client.delete('remove/{}'.format(str(new_user['username'])), headers = self.request_headers)
    response = delete_user_request.get_json()
    
    self.assertEqual(True, response)
    
    
  def test_get_user(self):
    
    new_user = {
      'username': self.faker.user_name(),
      'password': self.faker.password(),
      'user_type': UserType.CLIENT.value if randint(0, 9) % 2 == 0 else UserType.CLIENT_USER.value
    }
    
    register_user_request = self.client.post('register', data = json.dumps(new_user), headers = self.request_headers)
    response = register_user_request.get_json()
    
    self.assertEqual(True, response)
    
    get_user_request = self.client.get('user/{}'.format(str(new_user['username'])), headers = self.request_headers)
    print(get_user_request)
    response = get_user_request.get_json()
    
    self.assertEqual(response['username'], new_user['username'])
    self.assertEqual(response['user_type'], new_user['user_type'])
    
    delete_user_request = self.client.delete('remove/{}'.format(str(new_user['username'])), headers = self.request_headers)
    response = delete_user_request.get_json()
    
    self.assertEqual(True, response)