from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from flask_login import login_required

from app import create_app
from app.forms import LoginForm
from app.firestore_services import get_users, get_todos

app = create_app()

@app.cli.command()
def test():
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner().run(tests)

@app.errorhandler(500)
def internal_server_error(error):
  return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html', error=error)

@app.route('/')
def index():
  user_ip = request.remote_addr

  response = make_response(redirect('/hello'))
  #response.set_cookie('user_ip', user_ip)
  session['user_ip'] = user_ip

  return response

@app.route('/hello', methods=['GET'])
@login_required
def hello():
  #user_ip = request.cookies.get('user_ip')
  user_ip = session.get('user_ip')
  username = session.get('username')

  context = {
    'user_ip': user_ip,
    'todos': get_todos(username),
    'username': username
  }

  return render_template('hello.html', **context)
