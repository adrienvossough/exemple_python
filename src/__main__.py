import os  # module contenant des fonctions liées aux info sur l'OS
from . import init_app

# initialisation de l'application Flask
app = init_app()
# exemple d'utilisation des variables d'environnement
PORT = int(os.environ.get('SRV_PORT', 3000))
DEBUG = os.environ.get('SRV_DEBUG', True)
HOST = os.environ.get('SRV_HOST', '0.0.0.0')

# démarrage du serveur
app.run(host=HOST, port=PORT, debug=DEBUG)


