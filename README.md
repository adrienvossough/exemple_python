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

1. Faire une copie de sample.env et nommer cette copie en ".env" (sans les guillemets)
2. Modifier les variables contenues dans ".env"

3. A la racine du projet

    ```powershell
    # seulement la première fois
    py venv .venv

    # à chaque fois que l'on réouvre un nouveau terminal
    .\.venv\Scripts\Activate.ps1

    # la première fois
    pip install -r requirements
    ```

## Démarrage

```powershell
docker-compose up -d

$env:FLASK_APP = "app"
flask run
```
