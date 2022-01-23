# Simple projet en Python Flask

## Description

C'est un exemple de projet respectant des bonnes pratiques dans sa structure

## prérequis

* docker
* docker-compose
* python >=3.8
* pip
* venv
* git

## Installation

A la racine du projet

```powershell
# seulement la première fois
py venv .venv

# à chaque fois que l'on réouvre un nouveau terminal
.\.venv\Scripts\Activate.ps1

# la première fois
pyp install .
```

## Démarrage

```powershell
docker-compose up -d

$env:FLASK_APP = "app"
flask run
```
