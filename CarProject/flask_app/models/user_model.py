from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
#might need other imports like flash other classes and regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
db = 'exam'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.password = data['password']

#creates a new user and stores into database
    @classmethod
    def create_user(cls, form_data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        db_response = connectToMySQL(db).query_db(query, form_data)
        print(db_response)
        return db_response
    
#validates user and checks for length in forms and also if email is in correct format
    @staticmethod 
    def validate_user(form_data):
        is_valid = True
        if len(form_data['first_name']) < 3:
            flash('First name must be more than 3 characters')
            is_valid = False
        if len(form_data['last_name']) < 3:
            flash('Last name must be more than 3 characters')
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(form_data['password']) < 8:
            flash('Password needs to be more than 8 characters')
            is_valid = False
        if not PASSWORD_REGEX.match(form_data['password']):
            flash('Password needs to contain an uppercase and a number')
            is_valid = False
        return is_valid
    
#finds a user based on email of user
    @classmethod
    def find_user(cls, email_dict):
        query = "SELECT * from users WHERE email = %(email)s"
        db_response = connectToMySQL(db).query_db(query, email_dict)
        print(db_response)
        if len(db_response) < 1:
            return False
        return cls(db_response[0])