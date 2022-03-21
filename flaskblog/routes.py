from flask import redirect , render_template ,url_for,flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.model import User, Post
from flaskblog import app

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
