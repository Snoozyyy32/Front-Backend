from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from myapp.models import User
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(),
                                                     Length(min=2, max=20)])
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Passsword', validators =
                              [DataRequired(),])
    confirmed_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo(
        'password')])
    
    submit = SubmitField('Sign_up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken.Please use anaother username.')
        
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This email is taken.Please use anaother email.')
                                                        
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    password = PasswordField('Passsword', validators =
                              [DataRequired(),])
    remember = BooleanField('Remember_me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(),
                                                     Length(min=2, max=20)])
    email = StringField('Email',
                        validators = [DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
   
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username :
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken.Please use anaother username.')
            
    def validate_email(self, email):
        if email.data != current_user.email :
            user = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('This email is taken.Please use anaother email.')


class PostForm(FlaskForm):
    title = StringField('Title',validators = [DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post')

                                                                    