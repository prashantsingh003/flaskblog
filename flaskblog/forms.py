from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,Length,EqualTo, Email,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username=StringField('Username',
                        validators=[DataRequired(), Length(min=2,max=20)])
    email=StringField('Email',
                        validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is taken. Please take a diffrent name')
    
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email is taken. Please take a diffrent email')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')