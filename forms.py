from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from email_validator import validate_email, EmailNotValidError

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(),
                                                     Length(min=2, max=20)])
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Passsword', validators =
                              [DataRequired(),])
    confirmed_password = PasswordField('Confirmed_password', validators =
                              [DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign_up')
                                                        
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Passsword', validators =
                              [DataRequired(),])
    remember = BooleanField('Remember_me')
    submit = SubmitField('Login')
                                                     