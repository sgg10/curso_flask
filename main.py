import secrets
from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = secrets.token_urlsafe()

todos = ['Comprar cafe', 'Soliciutud de compra','Entregar el producto']

class LoginForm(FlaskForm):
  username = StringField('Nombre de usuario', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Enviar')

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

@app.route('/hello')
def hello():
  #user_ip = request.cookies.get('user_ip')
  user_ip = session.get('user_ip')
  context = {
    'user_ip': user_ip,
    'todos': todos,
    'login_form': LoginForm()
  }
  return render_template('hello.html', **context)
