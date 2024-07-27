from flask import Blueprint, request, render_template, redirect, session, flash
from .forms import Validator
from .services import Authentication

# Creating the Authentication Blueprint.
auth = Blueprint("auth", __name__, template_folder="templates/auth")

@auth.route("/register", methods=['GET', 'POST'])
def register():
    ''' Defining the Register Route'''
    
    questions = Authentication.get_questions()
    
    username_error = None
    password_error = None
    confirm_password_error = None
    email_error = None
    question_error = None
    answer_error = None
    
    if request.method == 'POST':
        
        # Retrieving the fields' data when the user uses the registration form.
        data = request.form
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        question_id = data.get("question-id")
        answer = data.get("answer")
        
        # Validating any errors with field in the registration form.
        username_error = Validator.username_validation(username)
        password_error = Validator.password_validation(password)
        confirm_password_error = Validator.confirm_password_validation(password, confirm_password)
        email_error = Validator.email_validation(email)
        question_error = Validator.question_validation(question_id)
        answer_error = Validator.answer_validation(answer)
        
        if not username_error and not password_error and not confirm_password_error and not email_error and not question_error and not answer_error:
            Authentication.register(username=username, password=password, email=email, question_id=question_id, answer=answer)
            return redirect("/login")
    
    return render_template("auth/register.html",
                        questions=questions,
                        username_error=username_error,
                        password_error=password_error,
                        confirm_password_error=confirm_password_error,
                        email_error=email_error,
                        custom_css='auth')
    
    
    
@auth.route("/login", methods=['GET', 'POST'])
def login():
    
    session.clear()
    login_error = None
    
    if request.method == 'POST':
        
        # Retrieving the fields' data when the user uses the login form.
        data = request.form
        email = data.get("email")
        password = data.get("password")
        
        # Validating any errors with field in the login form.
        login_error = Validator.login_validation(email, password)
        
        if login_error is None:
            user = Authentication.check_email(email)
            session['user_id'] = user.id
            return redirect('/')
    
    return render_template("auth/login.html", login_error=login_error, custom_css='auth')


@auth.route("/change", methods=['POST', 'GET'])
def change_password():
    session.clear()
    
    questions = Authentication.get_questions()
    
    errors = {
        'info': None,
        'password': None,
        'confirm_password': None
    }
    
    if request.method == 'POST':
        
        # Retrieving the fields' data when the user uses the change_password form.
        data = request.form
        email = data.get('email')
        question_id = data.get('question-id')
        answer = data.get('answer')
        password = data.get('password')
        confirm_password = data.get('confirm-password')
        
        # Validating any errors with field in the change_password form.
        errors['info'] = Validator.changepass_info_validation(email, question_id, answer)
        errors['password'] = Validator.password_validation(password)
        errors['confirm_password'] = Validator.confirm_password_validation(password, confirm_password)
        
        if not any(errors.values()):
            Authentication.change_password(email=email, question_id=question_id, answer=answer, password=password)
            flash("Password changed successfully!")
            return redirect("/login")
    
    return render_template("auth/change.html",
                           questions=questions,
                           errors=errors,
                           custom_css='auth')
    

@auth.route("/logout", methods=['GET'])
def logout():
    
    session.clear()
    return redirect("/")