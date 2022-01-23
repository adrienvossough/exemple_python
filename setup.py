# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# nous indiquons où chercher les fichiers
with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# va vérifier et lancer l'installation du projet
setup(
    name='app',
    version='0.1.0',
    description='Exemple de projet Python',
    long_description=readme,
    author='Adrien Vossough',
    author_email='adrien@semifir.com',
    url='https://www.semifir.com',
    license=license,
    packages=find_packages(where='src', exclude=('tests', 'docs')),
    install_requires=requirements,
)
