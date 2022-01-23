from flask import Flask
from flask_pymongo import PyMongo
from . import config

def init_app() -> Flask:
    """on crée une application "Flask"

    Returns:
        Flask: application "Flask" avec les routes
    """
    app = Flask(__name__, template_folder='views')
    # fonction qui charge l'ensemble des routes de notre serveur
    config.load_routes(app)
    return app


def init_db(app: Flask) -> PyMongo:
    """Initialise Pymongo avec Flask

    Args:
        app (Flask): Application Flask devant être connectée à la bdd

    Returns:
        PyMongo: ORM Mongo
    """
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    mongo = PyMongo(app)
    return mongo
