FROM python:3.8.3-buster

LABEL maintainer="adrien@semifir.com"


# Liste des variables d'environnement du conteneur
ENV FLASK_APP=/srv/web/
ENV SRV_PORT=3000
ENV MONGO_URI=mongodb://localhost:27017/myDatabase

# mise à jour du système
RUN apt update && apt upgrade -y

# mkdir /srv/flask && cd /srv/flask
WORKDIR /srv/flask

# le premier point correspond au répertoire courant au Dockerfile
# le second point correspond au répertoire /srv/flask dans le conteneur
# Grace au .dockerignore, Docker ne voit qu'une partie des fichiers et ne va donc pas tout copier
COPY . .

# on exécute l'installation de toutes les dépendances sur le conteneur
RUN pip install -r requirements.txt


# Permet d'ouvrir un port (3000) vers le conteneur
# Sans ce port, le conteneur est inaccessible par l'hôte
EXPOSE 3000

# la commande de base à executer lors du lancement d'un conteneur
ENTRYPOINT ["python"]
# complète la commande définie par ENTRYPOINT
CMD [ "-m", "src"]
# Commande finale = ENTRYPOINT["python"] + CMD ["-m", "app"]
# Si pas d'ENTRYPOINT :  Commande finale = CMD ["python", "-m", "app"]



