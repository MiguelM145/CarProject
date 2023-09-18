from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User 
from flask_app.models.cars_model import Cars
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#main login page
@app.route('/') #Get request for 127.0.0.1:5000
def home():
    return render_template('login.html')

#dashboard route, takes to main viewing page
@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    #sent user thru dashboard html for testing purposes most likely will want to send more data than just a session username this is also why i make this long so i remember to change it
    return render_template('dashboard.html', cars = Cars.get_cars())

#register route for user
@app.route('/register', methods=['POST']) #Post request route
def register():
    #validating if user info is valid if not redirecting back to main page and flashing
    if not User.validate_user(request.form):
        return redirect('/')
    #if password and confirm pw arent the same flashing warning and redirecting back to login
    if request.form['password'] != request.form['confirm_pw']:
        flash('Password and confirm password does not match')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash,
    }
    #user_id is recording newly created user id
    user_id = User.create_user(data)   
    
    if not user_id: 
        flash('Email already exists')
        return redirect('/')
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    return redirect('/dashboard')

#login route for user
@app.route("/login", methods = ['POST'])
def login_page():
    data ={
        'email': request.form['email']
    }
    user_in_db = User.find_user(data)
    if not user_in_db:
        flash("Invalid email/password!")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    return redirect("/dashboard")

#logout route, clears session and redirects back to login
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')