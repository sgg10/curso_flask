from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
  username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=5, max=30)])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
  submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
  description = StringField('Descripción', validators=[DataRequired()])
  submit_field = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
  submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
  submit = SubmitField('Actualizar')