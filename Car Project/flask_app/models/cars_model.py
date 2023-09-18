from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models import user_model
#might need other imports like flash other classes and regex

db = 'exam'

class Cars:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.desc = data['desc']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posted_by = None


#adds a car and stores into database
    @classmethod
    def add_car(cls, form_data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        db_response = connectToMySQL(db).query_db(query, form_data)
        print(db_response)
        return db_response
    
#validates car info 
    @staticmethod 
    def validate_car(form_data):
        is_valid = True
        if len(form_data['first_name']) < 3:
            flash('First name must be more than 3 characters')
            is_valid = False
        if len(form_data['last_name']) < 3:
            flash('Last name must be more than 3 characters')
            is_valid = False
    
#finds a car based on id
    @classmethod
    def find_user(cls, email_dict):
        query = "SELECT * from users WHERE email = %(email)s"
        db_response = connectToMySQL(db).query_db(query, email_dict)
        print(db_response)
        if len(db_response) < 1:
            return False
        return cls(db_response[0])
    
    #gets all cars and users
    @classmethod
    def get_cars(cls):
        query = "SELECT * FROM cars JOIN users ON users.id = cars.user_id"
        db_response = connectToMySQL(db).query_db(query)
        cars = []
        for user in db_response:
            new_car = cls(user)
            user_data = {
                'id': user['users.id'],
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'email': user['email'],
                'created_at': user['created_at'],
                'updated_at': user['updated_at'],
                'password': user['password']
            }
            new_car.posted_by = user_model.User(user_data)
            cars.append(new_car)
        return cars
    
    #gets a single car with user info
    @classmethod
    def get_car_w_user(cls, car_id):
        query = "SELECT * FROM users JOIN cars ON users.id = cars.user_id WHERE cars.id = %(id)s;"
        db_response = connectToMySQL(db).query_db(query, car_id)
        new_car = cls(db_response[0])
        new_car.posted_by = db_response[0]['first_name']
        print(new_car)
        return new_car
    
    #deletes car based on id fed into it
    @classmethod
    def delete(cls, car_id):
        query = "DELETE FROM cars WHERE id = %(id)s"
        db_response = connectToMySQL(db).query_db(query, car_id)
        print(db_response)
        return db_response

    #adds a car depending on form data fed into it
    @classmethod
    def add_car(cls, form_data):
        query = "INSERT INTO cars(user_id,model,make,year,`desc`,price) VALUES(%(user_id)s, %(model)s, %(make)s, %(year)s, %(desc)s, %(price)s);"
        db_response = connectToMySQL(db).query_db(query, form_data)
        return db_response
    
    #validates the add car form fits requirements
    @staticmethod 
    def validate_car(form_data):
        is_valid = True
        if int(form_data['price']) < 1:
            flash('Price must be atleast $1')
            is_valid = False
        if len(form_data['model']) < 1:
            flash('Model is required')
            is_valid = False
        if len(form_data['make']) < 1:
            flash('Make is required')
            is_valid = False
        if int(form_data['year']) < 1:
            flash('Year must be greater than 0')
            is_valid = False
        if len(form_data['desc']) < 1:
            flash('Description is required')
            is_valid = False
        return is_valid
    
    #checks that price and year are not empty to not return errors 
    @staticmethod
    def check_price_year(form_data):
        is_valid = True
        if len(form_data['price']) < 1:
            flash('Cant Leave Price Blank')
            is_valid = False
        if len(form_data['year']) < 1:
            flash('Cant Leave Year Blank')
            is_valid = False   
        return is_valid 
    
    #updates the car selected and runs query, also validates that the form fits all initial requirements
    @classmethod
    def update(cls, form_data):
        if not Cars.check_price_year(form_data):
            print('validation')
            return False
        if not Cars.validate_car(form_data):
            print('validated')
            return False
        query = "UPDATE cars SET model=%(model)s,make=%(make)s,year=%(year)s,`desc`=%(desc)s,price=%(price)s WHERE `id`= %(id)s;"
        db_response = connectToMySQL(db).query_db(query, form_data)
        return db_response