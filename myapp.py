from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm
from email_validator import validate_email, EmailNotValidError

# Create a Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd891e1593c0fd3bd1fc82ad93fbb184b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer(),unique = True,primary_key = True)
    username = db.Column(db.String(20),unique = True, nullable = False)
    email = db.Column(db.String(120),unique = True, nullable = False)
    img_file = db.Column(db.String(20), nullable = False,default = 'default.png')
    password = db.Column(db.String(60),nullable = False)
    posts = db.relationship('Post', backref='auther', lazy=True)
    def __repr__ (self):
        return f"User('{self.username}','{self.email}','{self.img_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer(),unique = True,primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'),nullable = False)
    def __repr__ (self):
        return f"Post('{self.title}','{self.date_postedl}'"

posts = [
{
    'author': 'Mike Murz',
    'title': 'First Blog Post',
    'content':'First post content',
    'date_posted': '2018/01/02'
}
,
{
    'author': 'David Tame',
    'title': 'Second Blog Post',
    'content':'Sirst post content',
    'date_psted': '2018/01/03'
}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash("You have been loged in successfully", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login was unsuccessfull !Please try again later.", 'danger')
    return render_template('login.html',title='Login', form=form)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

app.config['DEBUG'] = True

with app.app_context():
    # Now you can access the application and its extensions safely
    print(app.config['DEBUG'])
