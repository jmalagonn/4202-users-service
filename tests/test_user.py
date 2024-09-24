from unittest import TestCase
from faker import Faker
from flask import json
from app import app

class TestUser(TestCase):
  def setUp(self):
    self.client = app.test_client()
    self.faker = Faker()
    self.request_headers = {'Content-Type': 'application/json'}
    
  def test_register_user(self):
    new_user = {
      'username': self.faker.user_name(),
      'password': self.faker.password()
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
      'password': self.faker.password()
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