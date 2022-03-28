import re
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
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
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex,email.data):
            raise ValidationError('Please enter a valid email')
        if user:
            raise ValidationError('The email is taken. Please take a diffrent email')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

    def validate_email(self,email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        print(email.data)
        if not re.fullmatch(regex,email.data):
            raise ValidationError('Please enter a valid email')

class UpdateAccountForm(FlaskForm):
    username=StringField('Username',
                        validators=[DataRequired(), Length(min=2,max=20)])
    email=StringField('Email',
                        validators=[DataRequired()])
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jfif'])])                    
    submit=SubmitField('Update')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex,email.data):
            raise ValidationError('Please enter a valid email')
        if user:
            raise ValidationError('The email is taken. Please take a diffrent email')

    def validate_email(self,email):
        if email.data!=current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('The email is taken. Please take a diffrent email')

class PostForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content',validators=[DataRequired()])
    submit=SubmitField('Post')

class SearchForm(FlaskForm):
    searched=StringField('Searched',validators=[DataRequired()])
    submit=SubmitField('Submit')