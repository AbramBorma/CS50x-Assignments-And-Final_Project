from application.extensions import db
from application.Blueprints.auth.models import User, Questions
from werkzeug.security import check_password_hash

''' Creating the Authentication Class and its methods to handle all the operations on the Models'''

class Authentication:

    @staticmethod
    def register(username, email, password, question_id, answer):
        
        reg_user = User(username=username, email=email, question_id=question_id, answer=answer)
        reg_user.set_password(password)
        db.session.add(reg_user)
        db.session.commit()
        
    @staticmethod
    def login(email, password):
        login_user = User.query.filter_by(email=email).first()
        if login_user and check_password_hash(login_user.password_hash,password):
            return True
        return False

    @staticmethod
    def check_email(email):
        row = User.query.filter_by(email=email).first()
        return row
    
    @staticmethod
    def check_question(question_id):
        row = User.query.filter_by(question_id=question_id).first()
        return row
    
    @staticmethod
    def check_answer(answer):
        row = User.query.filter_by(answer=answer).first()
        return row

    @staticmethod    
    def check_username(username):
        row = User.query.filter_by(username=username).first()
        print (row)
        return row
    
    @staticmethod
    def change_password(email, question_id, answer, password):
        user = User.query.filter_by(email=email, question_id=question_id, answer=answer).first()
        if user:
            user.set_password(password)
            db.session.commit()
    
    @staticmethod
    def get_questions():
        return Questions.query.all()