import os
from flask import Flask
from flask_session import Session
from application.extensions import db
from application.Blueprints.main.controllers import main
from application.Blueprints.auth.controllers import auth
from application.Blueprints.venues.controllers import venue
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_pyfile('config.py')

Session(app)

db.init_app(app)

app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(venue)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
