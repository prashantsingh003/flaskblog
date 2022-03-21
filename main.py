from datetime import datetime
from email.policy import default
from flask import Flask, redirect , render_template ,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SECRET_KEY'] = 'nvd68a4fc168as46f'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref='author', lazy=True) 

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class ost():
    def __init__(self,author,title,content,date_posted):
        self.author=author
        self.title=title
        self.content=content
        self.date_posted=date_posted
    def __del__(self):
        print('The object is deleted')
    def __str__(self):
        return self.title+" BY "+self.author

list=[]
list.append(ost('Raman','The Story','the content','02-12-2005'))
list.append(ost('Simon','Never Say Never','Content','02-10-2000'))

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html',posts=list)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if(form.validate_on_submit()):
        flash(f'Account Created For {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=["GET","POST"])
def login():
    form=LoginForm()
    if(form.validate_on_submit()):
        if form.email.data == 'pk@blog.com' and form.password.data=='password':
            flash('logged in','success')
            return redirect(url_for('home'))
        else:
            flash('log in unseccess full','danger')
    return render_template('login.html',title='login',form=form)

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)