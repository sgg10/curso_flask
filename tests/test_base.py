from flask_testing import TestCase
from main import app
from flask import current_app, url_for

class MainTest(TestCase):

  def create_app(self):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    return app

  def test_app_exists(self):
    self.assertIsNotNone(current_app)

  def test_app_in_test_mode(self):
    self.assertTrue(current_app.config['TESTING'])

  def test_index_redirects(self):
    response = self.client.get(url_for('index'))

    self.assertRedirects(response, url_for('hello'))

  def test_hello_get(self):
    response = self.client.get(url_for('hello'))
    self.assert200(response)

  def test_hello_post(self):
    fake_user = {
      'username': 'fake-username',
      'password': 'fake-password'
    }
    response = self.client.post(url_for('hello'), data=fake_user)
    self.assertRedirects(response, url_for('index'))

  """def test_user_registered_flashed_message(self):
    fake_user = {
      'username': 'fake-username',
      'password': 'fake-password'
    }
    response = self.client.post(url_for('index'), data=fake_user)
    self.assert_message_flashed('Nombre de usuario registrado con éxito')"""
