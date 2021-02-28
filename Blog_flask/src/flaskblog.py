#import secrets
#key = secrets.token_hex(16)
from flask import Flask, render_template,flash, url_for, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e0b28e7439a3e007c5a41b5d8ce3d62c'
posts =[
   {
      'author': 'Maciej Jarystow',
      'title' : 'Blog post TEST',
      'content' : 'First post content',
      'date_posted' : 'February 21, 2021'
   },

   {
      'author': 'Adam Nowak',
      'title' : 'Blog post TEST part 2',
      'content' : 'Second post content',
      'date_posted' : 'February 21, 2021'
   },
]
@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', posts = posts)

@app.route('/about')
def about():
   return render_template('about.html', title='About')
@app.route('/register', methods =['GET','POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created for{form.username.data}!','success')
      return redirect(url_for('home'))
   return render_template('register.html', title= 'Register', form=form)

@app.route('/login', methods =['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      if form.email.data == 'admin@blog.com' and form.password.data =='password':
         flash("You have been logged in!", 'success')
         return redirect(url_for('home'))
      else:
         flash('Login Unsuccessfull. Please check username and password', 'danger')
   return render_template('login.html', title= 'Login', form=form)

if __name__ =='__main__':
   app.run(debug=True)
