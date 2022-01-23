from flask import Flask
import app.routes.math as api_math
import app.routes.web as web

def load_routes(app: Flask) -> None:
    """Permet de charger l'ensemble des routes sur une application Flask

    Args:
        app (Flask): Application Flask sur laquelle nous voulons ajouter des routes
    """
    app.register_blueprint(web.web_routes)
    app.register_blueprint(api_math.math)

