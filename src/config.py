from flask import Flask
from .routes import math as api_math
from .routes import web as pages

def load_routes(app: Flask) -> None:
    """Permet de charger l'ensemble des routes sur une application Flask

    Args:
        app (Flask): Application Flask sur laquelle nous voulons ajouter des routes
    """
    app.register_blueprint(pages.web_routes)
    app.register_blueprint(api_math.math)
