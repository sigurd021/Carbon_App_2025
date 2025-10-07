from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=2, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), length(min=2, max=30), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
