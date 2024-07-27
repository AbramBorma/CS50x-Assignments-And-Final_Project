import os
from dotenv import load_dotenv
load_dotenv()

DEBUG = True
TESTING = False
SECRET_KEY = os.getenv('SECRET_KEY')
SESSION_PERMANENT = False
SESSION_TYPE = 'filesystem'
SQLALCHEMY_DATABASE_URI = 'sqlite:////workspaces/57132653/project/application/explore.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
