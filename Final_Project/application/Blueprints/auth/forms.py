import re
from .services import Authentication

# Creating the Validator Class and its methods:
class Validator:
    
    # Defining a static method to validate the username field
    @staticmethod
    def username_validation(username):
        if not username:
            return 'Username is required' # Validating the username input field is not empty.
        
        elif Authentication.check_username(username) is not None:
            return 'Username is taken' # Validating that the username is not taken.
        
        return None
    
    # Defining a static method to validate the password field
    @staticmethod
    def password_validation(password):
        if not password:
            return 'Password is required' # Validating the password input field is not empty.
        
        elif len(password) < 8 or len(password) > 30:
            return 'Password must be between 8 and 30 characters' # Validating the password to be between 8 and 30 characters.
        
        elif not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-]).{8,}$', password):
            return 'Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character.'
        
        return None
    
    @staticmethod
    def confirm_password_validation(password, confirm_password):
        if not password:
            return 'Confirm Password' # Validating the confirm_password input field is not empty.
        
        elif password != confirm_password:
            return 'Passwords do not match' # Validating the match of the two passwords.
        
        return None
    
    # Defining a static method to validate the email input field
    @staticmethod
    def email_validation(email):
        if not email:
            return 'Email Address is required' # Validating the email input field is not empty.
        
        elif Authentication.check_email(email) is not None:
            return 'This email is already registered, please sign in' # Validating that the email is not registered.
        
        elif not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return 'Invalid email address.' # Validating that the email address is a valid one
        
        return None
    
    @staticmethod
    def question_validation(question_id):
        if not question_id:
            return 'Please select a security question'
        return None
    
    @staticmethod
    def answer_validation(answer):
        if not answer:
            return 'An answer for the security question is required'
        return None
    
    
    # Defining a static method to validate the login fields
    @staticmethod
    def login_validation(email, password):
        if not email:
            return 'Enter Email' # Validating the username/email input field is not empty.
        
        elif not password:
            return 'Enter the password' # Validating the password input field is not empty.
        
        elif Authentication.login(email, password) is False:
            return 'Invalid username/password' # Validating the username/email and password are registered.
        
        return None
    
    @staticmethod
    def changepass_info_validation(email, question_id, answer):
        ''' Validating the input fields in the Change Password form.'''
        
        errors = {}
        
        if not email:
            errors['email'] = 'Email Address is required!'
        elif not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            errors['email'] = 'Invalid email address!'
        elif Authentication.check_email(email) is None:
            errors['email'] = 'This email is not Registered!'
        
        if not question_id:
            errors['question_id'] = 'Please select a security question'
        elif Authentication.check_question(question_id) is None:
            errors['question_id'] = 'Incorrect security question'
        
        if not answer:
            errors['answer'] = 'An answer for the security question is required'
        elif Authentication.check_answer(answer) is None:
            errors['answer'] = "The security question's answer is incorrect"
        
        return errors