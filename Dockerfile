FROM python:3.8.3-buster

LABEL maintainer="adrien@semifir.com"

# fabrique le répertoire /srv/flask
# et se place dedans
WORKDIR /srv/flask
# le premier point correspond au répertoire courant au Dockerfile
# le second point correspond au répertoire /srv/flask dans le conteneur
# Grace au .dockerignore, Docker ne voit qu'une partie des fichiers et ne va donc pas tout copier
COPY . .
# on exécute l'installation de toutes les dépendances sur le conteneur
RUN pip install -r requirements.txt
# Liste des variables d'environnement du conteneur
ENV export FLASK_APP=/srv/web/
ENV SRV_PORT=3000
ENV MONGO_URI=mongodb://localhost:27017/myDatabase

# Permet d'ouvrir un port (3000) vers le conteneur
# Sans ce port, le conteneur est inaccessible par l'hôte
EXPOSE 3000

# la commande de base à executer lors du lancement d'un conteneur
ENTRYPOINT ["python"]
# complète la commande définie par ENTRYPOINT
CMD [ "-m", "app"]
# Commande finale = ENTRYPOINT["python"] + CMD ["-m", "app"]
# Si pas d'ENTRYPOINT :  Commande finale = CMD ["python", "-m", "app"]



