from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models.cars_model import Cars
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import pprint

#main login page
@app.route('/view/car/<int:car_id>') #Get request for 127.0.0.1:5000
def view_car(car_id):
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id': car_id
    }
    session['id'] = car_id
    return render_template('view_car.html', car = Cars.get_car_w_user(data))

#app route that takes in car id to delete the input
@app.route('/delete/<int:car_id>')
def delete_car(car_id):
    data={
        'id': car_id
    }
    Cars.delete(data)
    return redirect('/dashboard')

#route to add a new car, loads up add_car.html 
@app.route('/add/car')
def add_car():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('add_car.html')

#route that actually runs the query to add a car to our db
@app.route('/add_car', methods=['POST'])
def save_car(): 
    #checks if price or year are empty strings
    if not Cars.check_price_year(request.form):
        print('made it here')
        return redirect('/add/car')
    #checks for validation against the form requirements
    if not Cars.validate_car(request.form):
        return redirect('/add/car')
    data = {
        'user_id': session['user_id'],
        'price': request.form['price'],
        'model': request.form['model'],
        'make': request.form['make'],
        'year': request.form['year'],
        'desc': request.form['desc'],
    }
    Cars.add_car(data)
    return redirect('/dashboard')

#sends the car id and puts it in a session so we can edit also repopulates fields to edit
@app.route('/edit/car/<int:car_id>')
def edit_car(car_id):
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id' : car_id
    }
    session['id'] = car_id
    return render_template('edit_car.html', car = Cars.get_car_w_user(data))

#runs the update query to edit a cars post
@app.route('/update', methods = ['POST'])
def update():
    data = {
        'id' : session['id'],
        'price' : request.form['price'],
        'model' : request.form['model'],
        'make' : request.form['make'],
        'year' : request.form['year'],
        'desc' : request.form['desc']
    }
    if Cars.update(data) == False:
        print('whats it doing')
        return redirect(url_for('edit_car',car_id = session['id']))
    return redirect('/dashboard')