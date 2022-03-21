from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SECRET_KEY'] = 'nvd68a4fc168as46f'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

from flaskblog import routes