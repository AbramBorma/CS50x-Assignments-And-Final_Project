from flask import Blueprint, render_template

# Creating the main blueprint for the index page.
main = Blueprint('main', __name__, template_folder='templates')

@main.route("/")
def index():
    return render_template("index.html")

