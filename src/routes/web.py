from flask import render_template, Blueprint

web_routes = Blueprint('web', __name__)

@web_routes.route('/')
def index():
    return render_template('index.html')
